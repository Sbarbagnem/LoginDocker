FROM python:2.7-alpine3.7

ADD . /code
WORKDIR /code/

RUN apk --no-cache add --virtual build-dependencies \
    build-base \
    py-mysqldb \
    gcc \
    libc-dev \
    libffi-dev \
    mariadb-dev \
    && pip install -qq -r requirements.txt \
    && rm -rf .cache/pip \
    && apk del build-dependencies

RUN apk -q --no-cache add mariadb-client-libs

EXPOSE 8082

CMD ["python", "main.py"]
