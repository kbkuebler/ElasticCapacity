FROM python:3

WORKDIR /data

COPY requirements.txt ./
COPY capacity_collector.py /usr/local/bin
COPY rest-key.pem ./

RUN pip3 install --no-cache-dir -r requirements.txt


CMD /bin/sh -c 'while true; do python3 /usr/local/bin/capacity_collector.py; sleep ${refresh_seconds:-300}; done;'
