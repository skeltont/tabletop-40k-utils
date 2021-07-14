# tabletop utils

## Resources used

**The likeness of the faction icons do not belong to me. They are property of [Games Workshop](https://www.games-workshop.com/en-US/Home).**

The icons themselves were pulled from these sources:
- https://bakadesign.dk/warhammer-40-000-icons/
- https://github.com/Warhammer40kGroup/wh40k-icon
- and u/posixthreads on reddit

## Goals with the project

Web tool that will do things like:
- render uploaded battlescribe HTML rosters in a more manageable way
- generate match rules / settings
- dice roller (maybe, seems kind of overly done)
- custom rollable tables

## Local Setup
after pulling down the repo, add config
```
mkdir tabletop_utils/tabletop_utils/config;
```
set flask environment variable to use local config
```
export FLASK_ENV=development
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
