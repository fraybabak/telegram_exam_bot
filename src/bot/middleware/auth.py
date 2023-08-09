
from telegram import Update
from telegram.ext import CallbackContext
from di import userController
import json

def Auth(func):
    def wrapper(update: Update, context: CallbackContext):

        try:
            user = userController.find_by_external_id(update.effective_user.id)
            if user is None:
                user = update.effective_user
                user = userController.create(user.id, user.name, user.username, user.language_code, user.is_bot, False, user.first_name, user.last_name, user.link)
            
            context.user_data['internal_id'] = user.id

            result = func(update, context)
            return result
        except Exception as e:
            print(e)
            return update.message.reply_text("Please start the bot first")
    return wrapper