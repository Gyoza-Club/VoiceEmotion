FROM ubuntu:latest
dock

RUN apt-get update
RUN apt-get install -y python3 python3-pip

WORKDIR /usr/src/app
ENV FLASK_APP=app

COPY /app/requirements.txt ./

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
