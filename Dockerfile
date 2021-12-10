FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY requirements .
RUN apt update && pip install -U pip && pip install -r requirements
COPY . .
EXPOSE 8000
