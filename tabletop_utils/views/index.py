import os
import bcrypt
from flask import Blueprint, request, abort, render_template, redirect
from flask import current_app as app

from tabletop_utils import db
from tabletop_utils.models.user import User


@app.route("/", methods=["GET"])
def home():
    '''home page for the app'''

    return render_template("home.html")
