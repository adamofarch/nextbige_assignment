FROM python:3.11-alpine

ENV PYTHONUNBUFFERED=1
COPY ./requirements.txt /requirements.txt

RUN apk update && apk add --no-cache gcc musl-dev \
    libffi-dev postgresql-dev python3-dev build-base jpeg-dev zlib-dev 

RUN pip install -r requirements.txt

COPY . /app/
WORKDIR /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]



