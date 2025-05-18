# IoT Sensor Data Ingestion API

An API that processes incoming sensor data asynchronously, save it to the database, and allow retrieval of recent readings per device.

## Local Setup

1. Clone the repository

```bash
git clone git@github.com:WicklifeOguda/iot-sensor-api.git
```

2. Switch to the project directory

```bash
cd iot-sensor-api
```

3. Create and activate a virtual environment for isolating project dependencies

```bash
python3 -m venv venv

source venv/bin/activate

```

4. Install the requirements. requirements.txt for core dependencies. For full dev dependencies necessary for testing with pytest, use requirements-dev.txt instead.

```bash
pip install -r requirements.txt
```

OR

```bash
pip install -r requirements-dev.txt
```

5. Run and access the endpoint via http://127.0.0.1:8000

```bash
uvicorn app.main:app --reload
```

## Using Docker

Run

```bash
docker compose up
```

Access:
http://127.0.0.1:8000

## Sample Requests

1. Checking API health (if it is live)

```bash
curl http://localhost:8000/health
```

2. Creating SensorReading record

```bash

curl -X POST http://localhost:8000/readings \
  -H "Content-Type: application/json" \
  -d '{"device_id": "sensor-001", "temperature": 27.8, "humidity": 61.2, "timestamp": "2025-05-18T11:55:44Z"}'

```

3. Fetching Device's readings

```bash

curl http://localhost:8000/readings/sensor-001?limit=7

```

## Running unit tests locally

From the root directory, run:

```bash
pytest
```
