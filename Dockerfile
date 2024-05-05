FROM python:3.8.10-slim-buster

RUN apt-get update

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . ./

EXPOSE 8000

ENTRYPOINT ["gunicorn", "-k", "gevent", "-b", "0.0.0.0:8000", "project:create_app()"]
