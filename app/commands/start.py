from telegram import Update
from telegram.ext import CallbackContext

from .help_command import format_help_command


def start(update: Update, context: CallbackContext):
  reply = 'Hi there 🤘!'
  reply += '\n\n'
  reply += format_help_command()

  update.message.reply_markdown(
    reply,
    quote=False,
  )
