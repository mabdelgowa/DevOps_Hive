import requests
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    response = requests.get("https://api.opensensemap.org/boxes/5e60cf5557703e001bdae7f8?format=json")
    response = response.json()['sensors'][2]['lastMeasurement']['value']
    print(response)
    print(type(response))
    return {response}

#for index in req :


def print_version():
    print("current version is v0.0.1")


print_version()
