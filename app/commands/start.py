from telegram import ParseMode, Update
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext):
  text = 'Hi there 🤘! You can control me by sending these commands:'
  text += '\n\n'
  text += '/marco - 🧐'
  update.message.reply_text(text, parse_mode=ParseMode.MARKDOWN)
