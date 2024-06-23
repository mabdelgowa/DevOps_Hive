import requests
import prometheus_client
from fastapi import FastAPI, Response, status
from fastapi.testclient import TestClient
app = FastAPI()
from datetime import datetime

c = prometheus_client.Counter('my_response_total', 'HTTP Failures', ['method', 'endpoint'])

@app.get("/temperature")
def read_root():
    now = datetime.now()
    now = str(now.time())
    clock_hour_now = int(now[1])
    response1 = requests.get("https://api.opensensemap.org/boxes/5e60cf5557703e001bdae7f8?format=json")
    if response1.status_code == 200:
        c.labels('get', 'https://api.opensensemap.org/boxes/5e60cf5557703e001bdae7f8?format=json').inc()
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
    return "current version is v0.3.0"
@app.get("/metrics")
def send_metrics():
    return Response(
        media_type="text/plain",
        content=prometheus_client.generate_latest(),
    )



@app.get("/readyz")
def readyz():
    fastapi.ca
    response1 = requests.get("https://api.opensensemap.org/boxes/5e60cf5557703e001bdae7f8?format=json")
    response2 = requests.get("https://api.opensensemap.org/boxes/5eba5fbad46fb8001b799786?format=json")
    response3 = requests.get("https://api.opensensemap.org/boxes/5eb99cacd46fb8001b2ce04c?format=json")
    if str(response1) != "<Response [200]>" and str(response2) != "<Response [200]>" :
        return "HTTP != 200"
    elif str(response2) != "<Response [200]>" and str(response3) != "<Response [200]>" :
        return "HTTP != 200"
    elif str(response1) != "<Response [200]>" and str(response3) != "<Response [200]>" :
        return "HTTP != 200"
    else:
        return "HTTP = 200"

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
