
import logging, json

from telegram import __version__ as TG_VER

from di import contextController, userController, campaignController, questionController, answerController, scoreController
from bot.middleware.auth import Auth
try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
        Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


START_CAMPAIGN, SELECT_ANSWER = map(chr, range(2))
START_OVER, SELECT_CONTEXT = map(chr, range(3, 5))
END = map(chr, range(6, 7))
SHOWING = map(chr, range(7, 8))
STOPPING = ConversationHandler.END


# Define a few command handlers. These usually take the two arguments update and
# context.
@Auth
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Select an action: Adding parent/child or show data."""
    text = (
        "سلام، به ربات تست سایکو خوش آمدید. لطفا یکی از آزمون های زیر را انتخاب کنید."
    )
    exam_context = contextController.list_all()
    buttons = [
   [
        InlineKeyboardButton(text=exam.title, callback_data=json.dumps({
            't': 'start',
            'i': exam.id,
            'u': context.user_data['internal_id'],
        })) for exam in exam_context
    ],
    ]
    keyboard = InlineKeyboardMarkup(buttons)

    # If we're starting over we don't need to send a new message
    if context.user_data.get(START_OVER):
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(text=text, reply_markup=keyboard)
    else:
        await update.message.reply_text(
            "سلام، به ربات تست سایکو خوش آمدید. لطفا یکی از آزمون های زیر را انتخاب کنید.",
        )
        await update.message.reply_text(text=text, reply_markup=keyboard)

    context.user_data[START_OVER] = False

    return START_CAMPAIGN

def monitize_option(option):
    if option == 1:
        return 'کاملا مخالفم'
    elif option == 2:
        return 'مخالفم'
    elif option == 3:
        return 'متوسط'
    elif option == 4:
        return 'موافقم'
    elif option == 5:
        return 'کاملا موافقم'
    else:
        return 'نمیدانم'
        
def create_keyboard(question_number, context: ContextTypes.DEFAULT_TYPE):
    answer_range = range(1, 6)

    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(monitize_option(i), callback_data=
                json.dumps({
                    't': 'answer',
                    'a': i,
                    'q': question_number,
                    'u': context.user_data['internal_id'],

                }) 
            ) for i in answer_range
        ]
    ])


def pretty_print_question(question, bread_crumb):
    # Escape special characters for MarkdownV2
    escape_chars = '_*[]()~`>#+-=|{}.!'
    question = ''.join('\\' + char if char in escape_chars else char for char in question)
    bread_crumb = ''.join('\\' + char if char in escape_chars else char for char in bread_crumb)

    return f" {question} \n {bread_crumb} "

async def start_campaign(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Select an action: Adding parent/child or show data."""
    data = json.loads(update.callback_query.data)
    campaign = campaignController.create(data['u'], data['i'])
    questions = questionController.find_by_context_id(data['i'])
    context.user_data['current_state'] = {
        'campaign_id': campaign.id,
        'context_id': data['i'],
        'user_id': data['u'],
        'questions': [{
            'question_id': question.id,
            'question': question.question,
            
        } for question in questions],
        'current_question': 0,
        'answers': [],
    }
    return SELECT_ANSWER

async def send_result(update: Update, context: ContextTypes.DEFAULT_TYPE, file_path) -> None:
    with open(file_path, 'rb') as file:
        await context.bot.send_document(chat_id=update.effective_chat.id, document=file)


async def selecting_answers (update:Update, context: ContextTypes.DEFAULT_TYPE, data) -> None:
    current_state = context.user_data['current_state']
    if 'q' not in data and not data.get('q'):
        return await update.callback_query.edit_message_text(text=pretty_print_question(current_state['questions'][0]['question'] , f"{current_state['current_question']+1}/{len(current_state['questions'])}"), reply_markup=create_keyboard(question_number=0, context=context), parse_mode='MarkdownV2')
    current_state['current_question'] += 1
    if current_state['current_question'] == len(current_state['questions']):
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(text="در حال محاسبه نتیجه ...")
        calculate_score = scoreController.create(user_id=update.effective_user.id, campaign_id=current_state['campaign_id'])
        await send_result(update, context, calculate_score)
        await update.callback_query.edit_message_text(text="نتیجه آزمون شما ارسال شد.این آزمون صرفا جهت سنجش وضعیت روانی شما می باشد و نباید به عنوان تشخیص بیماری مورد استفاده قرار گیرد.")

        return STOPPING
    question = current_state['questions'][data['q']]
    answer = answerController.create(user_id=data['u'], question_id=question['question_id'], answer=data['a'], campaign_id=current_state['campaign_id'])
    current_state['answers'].append({
        'question_id': current_state['questions'][data['q']]['question_id'],
        'answer': data['a'],
    })
    return await update.callback_query.edit_message_text(text=pretty_print_question(current_state['questions'][data['q']+1]['question'] , f"{current_state['current_question']+1}/{len(current_state['questions'])}"), reply_markup=create_keyboard(question_number=data['q']+1, context=context))

@Auth
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query
    data = json.loads(query.data)
    if data['t'] == 'start':
        await start_campaign(update, context)
        await selecting_answers(update, context, data)
    elif data['t'] == 'answer':
        await selecting_answers(update, context, data)






@Auth
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")




@Auth
async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """End Conversation by command."""
    await update.message.reply_text("Okay, bye.")

    return END

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("6338311516:AAGT16kAZ1aMccnMonw_S7C-0PEMAPyFJ2Y").build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))

    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CallbackQueryHandler(button))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()