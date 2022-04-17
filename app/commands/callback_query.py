from telegram import Update
from telegram.ext import CallbackContext


def callback_query(update: Update, context: CallbackContext):
  query = update.callback_query
  query.answer()

  match query.data:
    case _:
      query.delete_message()
