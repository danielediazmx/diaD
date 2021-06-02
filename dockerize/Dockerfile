FROM python:3.7

RUN apt-get update \
    && apt-get install -y --no-install-recommends python-mysqldb

RUN apt-get install -y nano

RUN apt-get install -y mariadb-client && rm -rf /var/lib/apt && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

# RUN python manage.py makemigrations
# RUN python manage.py migrate

EXPOSE 8000

# Run command x
# CMD ["python", "manage.py", "migrate"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--insecure"]