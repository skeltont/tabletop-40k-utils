from flask import Blueprint, request, abort, jsonify
from flask import current_app as app

from tabletop_utils import db
from tabletop_utils.models.user import User

@app.route("/login", methods=["GET", "POST"])
def do_login():
    '''todo'''

    return jsonify({"hey": 'asdf'})
