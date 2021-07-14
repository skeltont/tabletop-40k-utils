'''application factory'''

# @todo: add point values to the lists

from pathlib import Path

from flask import Flask, redirect, session
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app(test_config=None):
    '''application factory'''

    app = Flask(__name__)
    if app.config['ENV'] == 'development':
        app.config.from_pyfile("config/default.py")
    else:
        app.config.from_pyfile("config/production.py")

    if test_config:
        app.config.update(test_config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    with app.app_context():
        # in order to make our app aware of our view routing.
        # pylint: disable=unused-import,import-outside-toplevel,unused-variable
        from tabletop_utils.views import login
        from tabletop_utils.views.wargaming import index, lists

        @app.route('/', methods=["GET"])
        def root_redirect():
            '''until real home page, redirect to wargaming'''

            return redirect('/wargaming')

        return app
