import os
import bcrypt
import boto3
from flask import Blueprint, request, abort, render_template, redirect
from flask import current_app as app

from tabletop_utils import db
from tabletop_utils.models.user import User


@app.route("/", methods=["GET"])
def home():
    '''home page for the app'''

    s3 = boto3.resource('s3')
    bucket = s3.Bucket('tabletoputils-upload')

    objects = list()

    for obj in bucket.objects.all():
        objects.append(obj)

    return render_template("home.html", objects=objects)
