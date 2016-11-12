FROM alpine

RUN echo http://nl.alpinelinux.org/alpine/edge/testing >> /etc/apk/repositories

RUN apk add --no-cache python3 python3-dev postgresql-dev musl-dev gcc gdal-dev
RUN pip3 install --upgrade pip

WORKDIR /home/app

COPY requirements /home/app/requirements

RUN /bin/sh -c 'pip3 install -r requirements/local.txt'

CMD python3 {{cookiecutter.project_slug}}/manage.py runserver_plus 0.0.0.0:8000
