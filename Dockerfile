FROM python:3.5.2

MAINTAINER Pietro Grandinetti
LABEL Description="Katie DJ -- katiedj.com"

RUN apt-get update \
  && apt-get install -y \
    python3-pip \
  && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# Ensure you have a file ./main/settings/secret.py
# in the local tree.
COPY . ./app

EXPOSE 8080

CMD cd /app && daphne -p 8080 main.asgi:application --bind 0.0.0.0 -v2
