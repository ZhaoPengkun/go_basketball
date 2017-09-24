from werkzeug.security import generate_password_hash, check_password_hash
from base import login_manager
from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    phone = db.Column(db.String(11))
    address = db.Column(db.String(128))
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)

    # def __init__(self, email, password):
    #     self.email = email
    #     self.password = password

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class Auth(db.Model):
    __tablename__ = 'auth'
    email = db.Column(db.String(64), primary_key=True, index=True)
    verification_code = db.Column(db.String(8))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
