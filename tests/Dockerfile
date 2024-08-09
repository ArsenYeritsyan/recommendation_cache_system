FROM python:3.9-slim

WORKDIR /app

COPY . /app
COPY tests.py /app
RUN apt-get update && apt-get install -y curl

RUN pip install --no-cache-dir requests redis

CMD ["python", "tests.py"]
