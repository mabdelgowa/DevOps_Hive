import requests
import prometheus_client
from fastapi import FastAPI, Response
app = FastAPI()
from datetime import datetime

@app.get("/temperature")
def read_root():
    now = datetime.now()
    now = str(now.time())
    clock_hour_now = int(now[1])
    response1 = requests.get("https://api.opensensemap.org/boxes/5e60cf5557703e001bdae7f8?format=json")
    response1 = float(response1.json()['sensors'][2]['lastMeasurement']['value'])
    response2 = requests.get("https://api.opensensemap.org/boxes/5eba5fbad46fb8001b799786?format=json")
    time_of_mesurement = response2.json()['sensors'][2]['lastMeasurement']['createdAt']
    response2 = float(response2.json()['sensors'][2]['lastMeasurement']['value'])
    response3 = requests.get("https://api.opensensemap.org/boxes/5eb99cacd46fb8001b2ce04c?format=json")
    response3 = float(response3.json()['sensors'][1]['lastMeasurement']['value'])
    response = (response1 + response2 + response3) // 3
    if response < 10:
        status = "Too_cold"
    elif response > 11 and response < 36:
        status = "good"
    else:
        status = "Too_hot"

    difference_in_time_between_mesurement_now = clock_hour_now - int(time_of_mesurement[12])
    print(response)
    return response, f'difference in time between mesurement now (hours) = {difference_in_time_between_mesurement_now}', status
@app.get("/version")
def print_version():
    return "current version is v0.0.1"

@app.get("/metrics")
def send_metrics():
    return Response(
        media_type="text/plain",
        content=prometheus_client.generate_latest(),
    )



