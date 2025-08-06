FROM python:3.11.4-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE='1'
ENV PYTHONUNBUFFERED='1'

WORKDIR /app/

RUN apt-get --allow-releaseinfo-change update

RUN apt-get update && apt-get install --no-install-recommends -y \
  build-essential \
  libpq-dev \
  git

RUN pip install --upgrade pip


COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

COPY ./compose/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY . /app/