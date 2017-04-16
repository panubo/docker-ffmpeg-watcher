FROM python:2.7

ENV PYTHONUNBUFFERED=0

WORKDIR /usr/src

ADD . /usr/src

RUN pip install -r requirements.txt

CMD ["python", "/usr/src/watcher.py"]
