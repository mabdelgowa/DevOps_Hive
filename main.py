import requests
import prometheus_client
from fastapi import FastAPI, Response
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
    boxes_id = ["5d8b36c15f3de0001abe60ea",
                "5d653fe8953683001a901323",
                "66506c7d96a6830008c33955",
                "67371eb8a5dfb4000700bda3"]
    urls= []
    for index_of_box_id in range(len(boxes_id)):
        urls.append("https://api.opensensemap.org/boxes/"+boxes_id[index_of_box_id]+"?format=json")
    result = []
    for index_of_url in range(len(urls)): 
        response =(requests.get(urls[index_of_url]))
        if  (response.status_code == 200) :
            for index_of_temperature_sensor in range(len(response.json()['sensors'])):
                if (response.json()['sensors'][index_of_temperature_sensor]["title"] == 'Temperatur'):
                    value_of_temperature= str(float(response.json()['sensors'][index_of_temperature_sensor]['lastMeasurement']['value']))
                    time_of_mesurement = response.json()['sensors'][index_of_temperature_sensor]['lastMeasurement']['createdAt']
                    result.append(value_of_temperature)
                    c.labels('get', index_of_url).inc()
    final_result_aggregiation = 0
    for index_of_result in result:
        final_result_aggregiation += float(index_of_result)
    final_result = round(final_result_aggregiation/len(result),2)
    # to detect the status of the temperature
    if final_result < 10:
            status = "Too_cold"
    elif final_result > 11 and response < 36:
            status = "good"
    else:
            status = "Too_hot"

    difference_in_time_between_mesurement_now = abs(clock_hour_now - int(time_of_mesurement[12])) # to be sure that the mesurement isn't older than one hour
    return final_result, f'difference in time between mesurement now (hours) = {difference_in_time_between_mesurement_now}', status




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
    boxes_id = ["5d8b36c15f3de0001abe60ea",
                "5d653fe8953683001a901323",
                "66506c7d96a6830008c33955",
                "67371eb8a5dfb4000700bda3"]
    urls= []
    http_error = "HTTP != 200 there is more than one box don't rsponse"
    response = "<Response [200]>"
    for index_of_box_id in range(len(boxes_id)):
        urls.append("https://api.opensensemap.org/boxes/"+boxes_id[index_of_box_id]+"?format=json")
    if str(requests.get(urls[1])) != response and str(requests.get(urls[2])) != response:
        return http_error
    elif str(requests.get(urls[3])) != response and str(requests.get(urls[2])) != response:
        return http_error
    elif str(requests.get(urls[1])) != response and str(requests.get(urls[3])) != response:
        return http_error
    else:
        return http_error
