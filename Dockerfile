FROM python:3.7

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        python-mysqldb \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y  \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

ADD starter.sh ./
RUN chmod +x ./starter.sh

EXPOSE 8000

CMD ["./starter.sh"]
