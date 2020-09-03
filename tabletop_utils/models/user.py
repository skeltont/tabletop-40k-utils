'''user model'''

from flask_login import UserMixin
from tabletop_utils import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(int(user_id))


class User(UserMixin, db.Model):
    '''user model'''

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
