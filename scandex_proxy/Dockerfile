FROM python:2.7.10

RUN pip install docker-py redis
RUN mkdir proxy

COPY dockerctl.py proxyserver.py redisdb.py /proxy/

WORKDIR /proxy

CMD python proxyserver.py
