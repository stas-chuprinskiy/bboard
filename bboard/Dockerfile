FROM python:3.10-alpine

WORKDIR /app
COPY . .
EXPOSE 8000

RUN apk add postgresql-client build-base postgresql-dev
RUN pip install -r requirements.txt
