'''landing page actions for the wargaming section of the site'''

from flask import render_template
from flask import current_app as app
from flask_login import login_required
from bs4 import BeautifulSoup

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


@app.route("/wargaming/lists/<string:list_name>", methods=["GET"])
@login_required
def show(list_name):
    '''home page for the app'''

    # ttutils_s3 = TTUtilsS3('tabletoputils-upload', prefix='wargaming/lists')
    # user_recents = ttutils_s3.list_user_objects(user='tybeast2000')
    # public_recents = ttutils_s3.list_user_objects(public=True)

    # @TODO: determine whether an s3 object can be loaded through the database
    # @TODO: `list_name` should be replaced with a primary key

    ttutils_s3 = TTUtilsS3('tabletoputils-upload', prefix='wargaming/lists')
    list_content = ttutils_s3.get_user_object(list_name)
    soup = BeautifulSoup(list_content)
    for s in soup(['script', 'style', 'br']):
        s.decompose()

    list_content = soup.prettify()


    return render_template("wargaming/show.html", list_content=list_content)
