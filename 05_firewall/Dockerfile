FROM python:3.9-slim

WORKDIR /app
COPY . /app

RUN pip install flask

RUN apt-get update && apt-get install -y iptables && apt-get clean

EXPOSE 8080

CMD ["python", "webpage.py"]