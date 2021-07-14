'''landing page actions for the wargaming section of the site'''

from flask import render_template, request
from flask import current_app as app
from flask_login import login_required
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import (
    validators, StringField, SelectField, BooleanField, IntegerField
)

from tabletop_utils.models import rosters

# from tabletop_utils.helpers.aws_s3 import TTUtilsS31


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


@app.route("/wargaming/lists/new", methods=["GET"])
@login_required
def new():
    '''provide the form for uploading a new list and setting tags for s3 object
    '''

    form = UploadForm()

    return render_template("wargaming/new.html", form=form)


@app.route("/wargaming/lists/create", methods=["POST"])
@login_required
def create():
    '''process the form provided for uploading an army list and storing it in S3
    '''

    print(request.form)
    form = UploadForm(request.form)

    return render_template("wargaming/new.html", form=form)
