import requests
import prometheus_client
from fastapi import FastAPI, Response, status
from fastapi.testclient import TestClient
from datetime import datetime

app = FastAPI()

c = prometheus_client.Counter('my_response_total', 'HTTP Failures',
                              ['method', 'endpoint'])  # this line for prometheus client to detect th HTTP requests



##########################This is the first path /version to return the current version########################

@app.get("/version")
def print_version():
    return "current version is v0.3.0"

##########################This is the second path /temperature which configured with three boxIDs########################
@app.get("/temperature")
def read_root():
    now = datetime.now()
    now = str(now.time())
    clock_hour_now = int(now[1])
    response1 = requests.get("https://api.opensensemap.org/boxes/5e60cf5557703e001bdae7f8?format=json")
    if response1.status_code == 200:
        c.labels('get', 'https://api.opensensemap.org/boxes/5e60cf5557703e001bdae7f8?format=json').inc()
        # used prometheus client to increment counter if the status code was 200
    response1 = float(response1.json()['sensors'][2]['lastMeasurement']['value'])
    response2 = requests.get("https://api.opensensemap.org/boxes/5eba5fbad46fb8001b799786?format=json")
    if response2.status_code == 200:
        c.labels('get', 'https://api.opensensemap.org/boxes/5eba5fbad46fb8001b799786?format=json').inc()
    time_of_mesurement = response2.json()['sensors'][2]['lastMeasurement']['createdAt']
    response2 = float(response2.json()['sensors'][2]['lastMeasurement']['value'])
    response3 = requests.get("https://api.opensensemap.org/boxes/5eb99cacd46fb8001b2ce04c?format=json")
    if response3.status_code == 200:
        c.labels('get', 'https://api.opensensemap.org/boxes/5eb99cacd46fb8001b2ce04c?format=json').inc()
    response3 = float(response3.json()['sensors'][1]['lastMeasurement']['value'])

    response = (response1 + response2 + response3) // 3 #to get the average of temperature
    # to detect the status of the temperature
    if response < 10:
        status = "Too_cold"
    elif response > 11 and response < 36:
        status = "good"
    else:
        status = "Too_hot"

    difference_in_time_between_mesurement_now = clock_hour_now - int(time_of_mesurement[12]) # to be sure that the mesurement isn't older than one hour
    print(response)
    return response, f'difference in time between mesurement now (hours) = {difference_in_time_between_mesurement_now}', status




##########################This is the third path /metrics to return default prometheus metrics and the configured metrics########################

@app.get("/metrics")
def send_metrics():
    return Response(
        media_type="text/plain",
        content=prometheus_client.generate_latest(),
    )

##########################This is the fourth path /readyz to returns HTTP 200 unless:50% + 1 of the configured senseBoxes are not accessible########################
@app.get("/readyz")
def readyz():
    response1 = requests.get("https://api.opensensemap.org/boxes/5e60cf5557703e001bdae7f?format=json")
    response2 = requests.get("https://api.opensensemap.org/boxes/5eba5fbad46fb8001b79978?format=json")
    response3 = requests.get("https://api.opensensemap.org/boxes/5eb99cacd46fb8001b2ce04c?format=json")
    if str(response1) != "<Response [200]>" and str(response2) != "<Response [200]>":
        return "HTTP != 200"
    elif str(response2) != "<Response [200]>" and str(response3) != "<Response [200]>":
        return "HTTP != 200"
    elif str(response1) != "<Response [200]>" and str(response3) != "<Response [200]>":
        return "HTTP != 200"
    else:
        return "HTTP = 200"




##########################This part for integration test to test all pathes at one time########################

client = TestClient(app)
def test_read_main():
    response = client.get("/temperature")
    assert response.status_code == 200
    response = client.get("/version")
    assert response.status_code == status.HTTP_200_OK
    assert response.text == '"current version is v0.3.0"'
    response = client.get("/metrics")
    assert response.status_code == status.HTTP_200_OK


test_read_main()
