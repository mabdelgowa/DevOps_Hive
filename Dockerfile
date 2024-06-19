FROM python:latest

WORKDIR /root/Desktop/

RUN pip install fastapi
RUN pip install uvicorn
RUN pip install requests


EXPOSE 80

#ENTRYPOINT [ "uvicorn", "main:app" ]

 
COPY main.py ./


CMD [ "fastapi", "run", "./main.py", "--port", "80" ] 
