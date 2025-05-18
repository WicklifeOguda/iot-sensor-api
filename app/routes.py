from typing import List

from fastapi import APIRouter, BackgroundTasks, Depends
from sqlalchemy.orm import Session

from . import crud_actions, schemas
from .database import SessionLocal

router = APIRouter()


# DB injection function
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/health")
def check_api_health():
    return {"status": "OK"}


@router.post("/readings", status_code=202)
def add_device_reading(
    data: schemas.IncomingSensorData,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
):
    """
    SensorReading creation endpoint
    """
    background_tasks.add_task(crud_actions.save_reading, db, data)
    return {"message": "Sensor reading received"}


@router.get("/readings/{device_id}", response_model=List[schemas.OutgoingSensorData])
def fetch_device_readings(
    device_id: str, limit: int = 10, db: Session = Depends(get_db)
):
    """
    Fetch endpoint for getting specific device's readings
    """
    # control limit
    if limit > 100:
        limit = 100

    return crud_actions.fetch_readings(db, device_id, limit)
