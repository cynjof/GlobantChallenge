# syntax=docker/dockerfile:1

FROM python:3.11-slim-bullseye

WORKDIR /python-docker

COPY app .

RUN pip install -r requirements.txt

CMD [ "python", "app.py", "--host=0.0.0.0"]