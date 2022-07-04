from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# this is being imported from INIT.py 




class Note(db.Model):
    id = db.Column(id.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date: db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unqiue=True)
    notes = db.relationships('Note')