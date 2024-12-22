from fastapi.testclient import TestClient
from main import app
from fastapi import status


client = TestClient(app=app)

##################this part to run unit test for each path and the returned status code ################################
def test_temp():
    response = client.get('/temperature')
    assert response.status_code == status.HTTP_200_OK


def test_ver():
    response = client.get('/version')
    assert response.status_code == status.HTTP_200_OK
    assert response.text == '"current version is v0.3.0"'
