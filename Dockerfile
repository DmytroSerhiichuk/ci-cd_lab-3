FROM python:3.12.0

WORKDIR /app

COPY /requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV PORT=8000
EXPOSE $PORT

RUN python manage.py migrate

CMD python manage.py runserver 0.0.0.0:$PORT