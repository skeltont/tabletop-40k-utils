FROM python:3.8-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

ENV FLASK_ENV production

COPY . .

# old CMD step before we needed to run migrations on deploy
# CMD ["gunicorn", "--bind", "0.0.0.0:3000", "wsgi:app", "--reload"]
RUN chmod u+x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
