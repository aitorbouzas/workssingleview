FROM python:3.7 as base

WORKDIR /var/server

COPY requirements.txt /var/server
RUN pip install --no-cache-dir -r requirements.txt -I
RUN pip install --no-cache-dir -U pip setuptools pip-tools

FROM base

WORKDIR /var/server
COPY . /var/server
