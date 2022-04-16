import os

from app import db, dispatcher
from app.db import test_db


def test_token():
  assert 'BOT_TOKEN' in os.environ

def test_dispatcher():
  assert dispatcher is not None
  assert dispatcher.bot is not None
  assert dispatcher.bot.token is not None

def test_db():
  assert db is not None
