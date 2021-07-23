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
- custom rollable tables

## Requirements
- relational database. uses RDS in prod, but you can use sqlite, mysql, etc.
- python 3.8
- aws s3 bucket access

## Local Setup
set flask environment variable to use local config
```
(linux) export FLASK_ENV=development
(powershell) $Env:FLASK_ENV="development"
```

create config file
```
touch tabletop_utils/tabletop_utils/config/default.py
```

replace `<values>` with yours
```
SECRET_KEY = "<your secret key>"

SQLALCHEMY_DATABASE_URI = '<database connection string>'
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
TEMPLATES_AUTO_RELOAD = True
```

install python dependencies

I recommend using [venv](https://docs.python.org/3/library/venv.html) to manage your project specific dependencies
```
pip install -r requirements.txt
```

apply migrations
```
flask db upgrade
```

If using vscode, create a launch.json file to run this in the debugger
```
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Flask",
            "type": "python",
            "request": "launch",
            "module": "flask",
            "env": {
                "FLASK_APP": "app.py",
                "FLASK_ENV": "development",
                "FLASK_DEBUG": "1"
            },
            "args": [
                "run"
            ],
            "jinja": true
        }
    ]
}
```

if not, you can run with
```
gunicorn --bind 0.0.0.0:3000 wsgi:app --reload
```

## Running the Container
build the image
```
docker build -f Dockerfile -t tabletop-utils .
```

run the container
```
sudo docker run --network=host -e FLASK_ENV=development tabletop_utils
```