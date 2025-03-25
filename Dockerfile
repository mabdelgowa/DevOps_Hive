FROM python:latest

WORKDIR /root/Desktop/
COPY requirements.txt main.py ./
RUN pip install -r requirements.txt
RUN useradd --uid 1000 newuser
EXPOSE 80
USER newuser
CMD [ "fastapi", "run", "./main.py", "--port", "80" ] 
