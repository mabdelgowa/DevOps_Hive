FROM python:latest

WORKDIR /root/Desktop/

RUN pip install fastapi
RUN pip install uvicorn

EXPOSE 8000

ENTRYPOINT [ "uvicorn", "main:app", "--reload" ]

 
COPY main.py ./


CMD [ "python", "./main.py" ]
