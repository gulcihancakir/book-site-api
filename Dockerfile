FROM python:3.7.2-slim

WORKDIR /app
COPY requirements.txt /app
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    build-essential \
    ntp \
    python3-dev \
    python3-setuptools \
    mysql-client \
    default-libmysqlclient-dev && \
    rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip

RUN pip install -r requirements.txt 
    
COPY . /app
