FROM python:3.7

WORKDIR /usr/local/src

RUN pip install --upgrade pip

COPY requirements.txt /usr/local/src

RUN pip install -r /usr/local/src/requirements.txt

ENTRYPOINT [ "python", "main.py" ]

CMD [ "--help" ]