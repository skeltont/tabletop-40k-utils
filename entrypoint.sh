#!/usr/bin/env bash
flask db upgrade
gunicorn --bind 0.0.0.0:3000 wsgi:app --reload
