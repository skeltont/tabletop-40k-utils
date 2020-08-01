# tabletop utils

Web tool that will do things like:
- render uploaded rosters in a more manageable way
- generate match rules / settings
- dice roller (maybe, seems kind of overly done)
- whatever else sounds cool

## Local Setup
after pulling down the repo, add config
```
mkdir tabletop_utils/tabletop_utils/config;
```
create config file
```
vim tabletop_utils/tabletop_utils/config/default.py
```
replace `<values>` with yours
```
SECRET_KEY = "<secret_key>"

SQLALCHEMY_DATABASE_URI = '<sqlite_uri>'
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
```

## Local running
```
docker-compose up
```
