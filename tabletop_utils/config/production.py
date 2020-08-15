import os

SECRET_KEY = "TODO"

sql_host = os.environ.get("SQL_HOST")
sql_pass = os.environ.get("SQL_PASS")

SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://ttdev:{sql_pass}@{sql_host}/tabletop_utils'
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
