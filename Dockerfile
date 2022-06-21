FROM python:3.7

WORKDIR /app

RUN pip install flask
RUN pip install xmltodict

CMD [ "python", "main.py" ]