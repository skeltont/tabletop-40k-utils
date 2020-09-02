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

    client = boto3.client('s3')

    response = client.list_objects(
        Bucket='tabletoputils-upload'
    )

    recents = list()
    for obj in response['Contents']:
        tags = client.get_object_tagging(
            Bucket='tabletoputils-upload',
            Key=obj['Key']
        )

        list_obj = dict()
        for tag in tags['TagSet']:
            # if tag['Key'] == 'faction':
            #     print(tag['Value'])
            #     recents.append(tag['Value'])
            list_obj[tag['Key']] = tag['Value']
        recents.append(list_obj)

    print(recents)

    return render_template("home.html", recents=recents)
