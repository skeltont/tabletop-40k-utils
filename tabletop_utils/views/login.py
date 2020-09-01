'''login view'''

import bcrypt
from flask import request, render_template, redirect, session
from flask import current_app as app
from flask_wtf import FlaskForm
from wtforms import validators, PasswordField, StringField

from tabletop_utils import db
from tabletop_utils.models.user import User


class LoginForm(FlaskForm):
    '''form object for the login page'''

    username = StringField('username', validators=[
        validators.DataRequired()
    ])
    password = PasswordField('password', validators=[
        validators.DataRequired()
    ])


@app.route("/login", methods=["GET", "POST"])
def login():
    '''handle the submitted login form'''

    form = LoginForm(request.form)

    if request.method == "GET":
        return render_template("login.html", form=form)

    if form.validate():
        user = db.session.query(User).\
            filter(User.username == form.username.data).first()

        if not user:
            return redirect('/login')

        form_pass_enc = form.password.data.encode('utf-8')
        user_pass_enc = user.password.encode('utf-8')
        if bcrypt.checkpw(form_pass_enc, user_pass_enc):
            session["user_id"] = user.id

            return redirect('/')

    return render_template("login.html", form=form)
