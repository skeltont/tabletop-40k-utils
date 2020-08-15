import os

SECRET_KEY = "TODO2"

sql_info = os.environ.get("SQL_INFO")
sql_info_dict = json.loads(sql_info)

SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://ttdev:{sql_info_dict['password']}@{sql_info_dict['host']}/tabletop_utils'
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
