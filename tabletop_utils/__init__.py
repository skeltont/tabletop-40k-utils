'''application factory'''



from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(test_config=None):
    '''application factory'''

    app = Flask(__name__)
    app.config.from_pyfile("config/production.py")

    if test_config:
        app.config.update(test_config)

    db.init_app(app)
    with app.app_context():
        # in order to make our app aware of our view routing.
        # pylint: disable=unused-import,import-outside-toplevel
        from tabletop_utils.views import login, index

        return app
