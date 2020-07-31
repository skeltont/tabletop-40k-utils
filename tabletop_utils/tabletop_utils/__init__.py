from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(test_config=None):
    '''application factory'''

    app = Flask(__name__)
    app.config.from_pyfile("config/default.py")

    if test_config:
        app.config.update(test_config)

    db.init_app(app)
    with app.app_context():
        from tabletop_utils.views import login

        db.create_all()

        return app
