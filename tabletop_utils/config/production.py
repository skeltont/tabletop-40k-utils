import os
# import json

SECRET_KEY = "TODO2"

sql_info = os.environ.get("SQL_INFO")
print(sql_info)
# sql_info_dict = json.loads(sql_info)

# sql_pass = sql_info_dict['password']
# sql_host = sql_info_dict['host']

# SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://admin:{sql_pass}@{sql_host}/tabletop_utils'
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
