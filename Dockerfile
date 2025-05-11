FROM python:latest
RUN useradd --uid 1000 newuser
WORKDIR /home/newuser
COPY requirements.txt main.py ./
RUN pip install -r requirements.txt
EXPOSE 80
USER newuser
CMD [ "fastapi", "run", "./main.py", "--port", "80" ] 
