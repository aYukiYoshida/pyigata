FROM python:3.7

WORKDIR /opt/src

RUN pip install --upgrade pip

COPY requirements.txt /opt/src

RUN pip install -r /opt/src/requirements.txt

ENTRYPOINT [ "python", "main.py" ]

CMD [ "--help" ]