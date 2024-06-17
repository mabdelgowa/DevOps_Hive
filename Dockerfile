FROM python:latest

WORKDIR ~/Desktop

 
COPY main.py ./


CMD [ "python", "./main.py" ]
