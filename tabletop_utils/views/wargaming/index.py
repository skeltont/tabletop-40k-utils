'''landing page actions for the wargaming section of the site'''

from flask import render_template
from flask import current_app as app
from flask_login import login_required

from tabletop_utils.helpers.aws_s3 import TTUtilsS3


@app.route("/wargaming", methods=["GET"])
@login_required
def home():
    '''home page for the app'''

    ttutils_s3 = TTUtilsS3('tabletoputils-upload', prefix='wargaming/lists')
    user_recents = ttutils_s3.list_user_objects(user='tybeast2000')
    public_recents = ttutils_s3.list_user_objects(public=True)

    return render_template(
        "wargaming/home.html",
        public_recents=public_recents, user_recents=user_recents
    )
