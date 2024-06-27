FROM python:latest

WORKDIR /root/Desktop/
COPY requirements.txt main.py ./
RUN pip install -r requirements.txt

EXPOSE 80


 




CMD [ "fastapi", "run", "./main.py", "--port", "80" ] 
