from sqlaclhemy import event
from app.database import db

class User(db.Model):
    __tablename__='user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable = False, unique=True)
    dob
