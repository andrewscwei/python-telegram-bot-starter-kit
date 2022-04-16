from .db import db


class Foo(db.Model):
  __tablename__ = 'foos'

  id = db.Column(db.Integer, primary_key=True)
  chat_id = db.Column(db.Integer)
  created_at = db.Column(db.DateTime, server_default=db.func.now())
  updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

  def __init__(self, chat_id):
    self.chat_id = chat_id
