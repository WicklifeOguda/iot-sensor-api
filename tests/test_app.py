from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_check_api_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}


def test_add_device_reading():
    payload = {
        "device_id": "sensor-001",
        "temperature": 28.5,
        "humidity": 62.2,
        "timestamp": "2025-05-18T08:53:38Z",
    }
    response = client.post("/readings", json=payload)
    assert response.status_code == 202
    assert response.json() == {"message": "Sensor reading received"}


def test_fetch_device_readings():
    response = client.get("/readings/sensor-001")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
