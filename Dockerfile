FROM panubo/s3fs:latest

ENV PYTHONUNBUFFERED=0

WORKDIR /usr/src

# add python
RUN apt-get update && \
    apt-get -y install python-pip python-dev libyaml-dev && \
    apt-get -y clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD . /usr/src

RUN pip install -r requirements.txt

CMD ["python", "/usr/src/watcher.py"]
