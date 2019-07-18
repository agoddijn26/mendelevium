FROM python:3.6-slim

LABEL maintainer="alexander.goddijn@n26.com"

WORKDIR /app
ADD . /app

RUN pip install pipenv                  \
    && pipenv install

EXPOSE 5000
CMD pipenv run flask run