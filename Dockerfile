FROM python:3.13.0-alpine

RUN apt update && apt upgrade -y
RUN apt install python3-pip -y
RUN pip3 install -U pip
COPY . /app
WORKDIR /app
RUN pip3 install -U -r requirements.txt
CMD flask run
