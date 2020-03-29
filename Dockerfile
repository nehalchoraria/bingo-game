FROM python:3.7-slim-buster
RUN apt-get update -y
RUN apt-get install -y python3
RUN apt-get install -y python-pip python-dev build-essential

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app
RUN pip install -r requirements.txt

COPY . /app
EXPOSE 80

CMD ["uwsgi","app.ini"]
