'''landing page actions for the wargaming section of the site'''

from flask import render_template
from flask import current_app as app
from flask_login import login_required
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, SelectField, BooleanField

# from tabletop_utils.helpers.aws_s3 import TTUtilsS31


# class UploadForm(FlaskForm):
#     '''form object for uploading a list and it's details'''

#     upload = FileField('upload', validators=[
#         FileRequired(),
#         FileAllowed(['html'], 'HTML files only!')
#     ])
#     name =


@app.route("/wargaming/lists/new", methods=["GET"])
@login_required
def new():
    '''provide the form for uploading a new list and setting tags for s3 object
    '''

    # form = UploadForm()

    return render_template("wargaming/new.html")
