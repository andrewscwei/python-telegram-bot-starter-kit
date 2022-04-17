from telegram import Update
from telegram.ext import CallbackContext


def help_command(update: Update, context: CallbackContext):
  update.message.reply_markdown(
    format_help_command(),
    quote=False,
  )

def format_help_command() -> str:
  ret = 'You can control me by sending these commands:'
  ret += '\n\n'
  ret += '/marco - 🧐'

  return ret
