import os


def test_bot_token():
  assert 'BOT_TOKEN' in os.environ
