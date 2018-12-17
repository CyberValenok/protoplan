from dl import db
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120),index=True, unique=True)
    password= db.Column(db.String(128))

    #def __perp__(self):
    #    return '<User <>'.format(self.username)
#
#    def set_password(self, password):
##    def check_password()
