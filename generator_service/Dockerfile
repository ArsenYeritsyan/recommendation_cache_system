FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install feedparser flask

CMD ["python", "generator.py"]
