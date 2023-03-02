FROM python:3.7-slim

WORKDIR /app
COPY . /app

COPY app/models/lgbm_classifier.pickle ./app/models/

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8080
ENV PORT 8080

CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 app:app
