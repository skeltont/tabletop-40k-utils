FROM python:3.8
WORKDIR /app

ARG sql_host
ENV SQL_HOST=${sql_host}

ARG sql_pass
ENV SQL_PASS=${sql_pass}

ARG sql_test
ENV SQL_TEST=${sql_test}}

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD ["gunicorn", "--bind", "0.0.0.0:3000", "wsgi:app", "--reload"]
