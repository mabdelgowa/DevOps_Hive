from fastapi.testclient import TestClient
from fastapi import status
from main import app   
##########################This part for integration test to test all pathes at one time########################

client = TestClient(app)
def test_read_main():
    response = client.get("http://127.0.0.1/temperature")
    assert response.status_code == 200
    response = client.get("http://127.0.0.1/version")
    assert response.status_code == status.HTTP_200_OK
    assert response.text == '"current version is v0.3.0"'
    response = client.get("http://127.0.0.1/metrics")
    assert response.status_code == status.HTTP_200_OK


test_read_main()