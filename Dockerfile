FROM python:latest

WORKDIR /root/Desktop/
RUN pip install -r requirements.txt

EXPOSE 80


 
COPY requirements.txt main.py ./


CMD [ "fastapi", "run", "./main.py", "--port", "80" ] 
