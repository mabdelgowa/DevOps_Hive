from fastapi.testclient import TestClient
from fastapi import status
from context import main
##########################This part for integration test to test all pathes at one time########################

client = TestClient(main.app)
def test_read_main():
    response = client.get("/temperature")
    assert response.status_code == 200
    response = client.get("/version")
    assert response.status_code == status.HTTP_200_OK
    assert response.text == '"current version is v0.3.0"'
    response = client.get("/metrics")
    assert response.status_code == status.HTTP_200_OK


test_read_main()
