FROM python:3

WORKDIR /app/api
COPY requirements.txt /app/api
RUN pip3 install -r requirements.txt
COPY ./api /app/api/