FROM python:2.7

ADD . /code
WORKDIR /code/

RUN pip install -r requirements.txt


EXPOSE 8082

CMD python /code/app/app.py && python /code/app/test.py
