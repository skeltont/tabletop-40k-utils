'''landing page actions for the wargaming section of the site'''

from flask import json, render_template, request, abort, jsonify
from flask import current_app as app
from flask_login import current_user, login_required
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from sqlalchemy import sql
from wtforms import (
    validators, StringField, SelectField, BooleanField, IntegerField
)
from sqlalchemy.exc import SQLAlchemyError
from bs4 import BeautifulSoup

from tabletop_utils import db
from tabletop_utils.models import Roster, User
from tabletop_utils.helpers.aws_s3 import TTUtilsS3


class UploadForm(FlaskForm):
    '''form object for uploading a list and it's details'''

    upload = FileField('upload', validators=[
        FileRequired(),
        FileAllowed(['html'], 'HTML files only!')
    ])
    name = StringField('name', validators=[
        validators.DataRequired(),
        validators.Length(max=50)
    ])
    points = IntegerField('points', validators=[
        validators.DataRequired()
    ])
    faction = SelectField('faction', validators=[
        validators.DataRequired(),
    ], choices=[
        ('adepta-sororitas', 'Adepta Sororitas'),
        ('adeptus-astartes', 'Adeptus Astartes'),
        ('adeptus-mechanicus', 'Adeptus Mechanicus'),
        ('astra-militarum', 'Astra Militarum'),
        ('asuryani', 'Asuryani'),
        ('chaos-daemons', 'Chaos Daemons'),
        ('drukhari', 'Drukhari'),
        ('dark-mechanicum', 'Dark Mechanicum'),
        ('genestealer-cults', 'Genestealer Cults'),
        ('heretic-astartes', 'Heretic Astartes'),
        ('necrons', 'Necrons'),
        ('orks', 'Orks'),
        ('tau', 'Tau'),
        ('tyranids', 'Tyranids')
    ])
    public = BooleanField('public', validators=[
        validators.Optional()
    ])


@app.route("/wargaming/rosters", methods=["GET"])
@login_required
def index():
    '''home page for the app'''

    public_recents = Roster.query.join(User).\
        filter(Roster.public).\
        order_by(Roster.create_datetime)
    user_recents = Roster.query.join(User).\
        filter(Roster.user_id == current_user.id).\
        order_by(Roster.create_datetime)

    return render_template(
        "wargaming/index.html",
        public_recents=public_recents, user_recents=user_recents
    )


@app.route("/wargaming/rosters/<int:roster_id>", methods=["GET"])
@login_required
def show(roster_id):
    '''home page for the app'''

    roster = Roster.query.join(User).\
        filter(Roster.id == roster_id).one_or_none()

    if not roster or roster.user.id != current_user.id:
        abort(405)

    ttutils_s3 = TTUtilsS3('tabletoputils-upload', prefix='wargaming/rosters')
    uploaded_html = ttutils_s3.get_user_object(roster.object)

    soup = BeautifulSoup(uploaded_html)
    for s in soup(['script', 'style', 'br']):
        s.decompose()

    roster_content = soup.prettify()

    return render_template("wargaming/show.html", roster_content=roster_content)


@app.route("/wargaming/rosters/new", methods=["GET"])
@login_required
def new():
    '''provide the form for uploading a new list and setting tags for s3 object
    '''

    form = UploadForm()

    return render_template("wargaming/new.html", form=form)


@app.route("/wargaming/rosters/create", methods=["POST"])
@login_required
def create():
    '''process the form provided for uploading an army list and storing it in S3
    '''

    # @TODO: scrape scripts, brs, and styling out immediately

    form = UploadForm(request.form)

    return render_template("wargaming/new.html", form=form)


@app.route("/wargaming/rosters/<int:roster_id>/make_public", methods=["PUT"])
@login_required
def make_public(roster_id):
    '''process the form provided for uploading an army list and storing it in S3
    '''

    roster = Roster.query.join(User).\
        filter(Roster.id == roster_id).one_or_none()

    if not roster or roster.user.id != current_user.id:
        abort(405)

    try:
        roster.public = not roster.public
        db.session.commit()
    except SQLAlchemyError as err:
        print(f"failed to update public status for roster{roster.id}: {err}")
        db.session.rollback()

    return jsonify({"op": "success"})
