FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install requests redis flask

CMD ["python", "invoker.py"]
