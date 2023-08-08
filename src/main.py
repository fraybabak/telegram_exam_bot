
import logging

from telegram import __version__ as TG_VER

from di import contextController, userController, binaryCampaignController
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
        "Welcome To sycho Test, Please select Quiz test. To abort, simply type /stop."
    )
    exam_context = contextController.list_all()
    buttons = [
        [
            InlineKeyboardButton(text="Select Quiz", callback_data=str(START_CAMPAIGN)),
        ],
    ]
    keyboard = InlineKeyboardMarkup(buttons)

    # If we're starting over we don't need to send a new message
    if context.user_data.get(START_OVER):
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(text=text, reply_markup=keyboard)
    else:
        await update.message.reply_text(
            "Hi, I'm Sycho Test Bot. I can help you to know your mental health. "
        )
        await update.message.reply_text(text=text, reply_markup=keyboard)

    context.user_data[START_OVER] = False

    return START_CAMPAIGN

@Auth
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")


@Auth
async def start_campaign(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    try:
        
        exam_context = contextController.create(update.message.text)
        campaign = binaryCampaignController.create(context.user_data['internal_id'], exam_context.id)

        await update.message.reply_text({
           "campaign_id": campaign.id,
              "exam_context_id": exam_context.id,
                "user_id": context.user_data['internal_id'],

        })
    except Exception as e:
        await update.message.reply_text(e)


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
    application.add_handler(CommandHandler('START_CAMPAIGN', start_campaign))

    # on non command i.e message - echo the message on Telegram
    # application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, createContext))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()