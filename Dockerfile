FROM python:latest

WORKDIR /root/Desktop/

RUN pip install fastapi

RUN pip install requests

RUN pip install  prometheus-client

RUN pip install datetime
EXPOSE 80


 
COPY main.py ./


CMD [ "fastapi", "run", "./main.py", "--port", "80" ] 
