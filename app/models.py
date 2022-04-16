from .db import db


class SomeEntity(db.Model):
  __tablename__ = 'some_entities'

  id = db.Column(db.Integer, primary_key=True)

  def __init__(self):
    pass
