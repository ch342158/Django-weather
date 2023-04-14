FROM python:3.10

ENV SERVER_URL '${SERVER_URL}'
ENV STATIC_URL '${SERVER_URL}'

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    python3-dev postgresql-client build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./exam .
#COPY ./exam/WeatherApi.py .

ENV DB_NAME finalexam
ENV DB_USER root
ENV DB_PASSWORD 400168246
ENV DB_HOST localhost
ENV DB_PORT 3306

CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:8000"]


