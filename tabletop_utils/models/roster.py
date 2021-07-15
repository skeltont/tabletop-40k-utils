'''roster model for wargaming 40k rosters tracked in the db once uploaded'''

import datetime

from tabletop_utils import db


class Roster(db.Model):
    '''roster model'''

    __tablename__ = 'rosters'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(80), unique=True, nullable=False)
    faction = db.Column(db.String(80))
    object = db.Column(db.String(80), unique=True, nullable=False)
    public = db.Column(db.Boolean, default=False, nullable=False)
    create_datetime = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    user = db.relationship("User")
