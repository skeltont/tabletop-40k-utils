import os

from flask import Blueprint, request, abort, render_template, redirect
from flask import current_app as app

from tabletop_utils import db
# from tabletop_utils.models.user import User

@app.route("/login", methods=["GET", "POST"])
def do_login():
    '''todo'''

    sql_info = os.environ.get("SQL_INFO")

    # if request.method == "POST"
    #     return redirect()

    users = db.session.query(User)

    return render_template("login.html", users=users, sql_info=sql_info)
