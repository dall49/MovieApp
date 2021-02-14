
FROM python:alpine

WORKDIR /app

COPY . .

RUN pip install --upgrade pip && pip install pipenv && pipenv install --system

EXPOSE 8000

CMD gunicorn --timeout 60 -w $((`nproc`*2+1)) -b 0.0.0.0:8000 "run:create_app()"
