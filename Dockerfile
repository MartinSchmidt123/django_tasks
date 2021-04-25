FROM python:3.8-slim-buster

RUN mkdir /app
WORKDIR /app
ENV PYTHONUNBUFFERED 1

COPY Pipfile Pipfile.lock /app/
RUN pip install pipenv && \
    pipenv install --system

ADD . /app/

EXPOSE 8000

CMD python manage.py migrate && \
    python manage.py collectstatic --noinput && \
    python manage.py runserver 0.0.0.0:8000
