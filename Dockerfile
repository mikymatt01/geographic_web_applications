# syntax=docker/dockerfile:1
FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code

RUN apt-get update && apt-get install -y binutils libproj-dev gdal-bin

RUN python3.9 -m pip install --upgrade pip
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt

COPY . /code/

ENV USE_POSTGRES=TRUE

CMD gunicorn geodjango.wsgi --log-file -