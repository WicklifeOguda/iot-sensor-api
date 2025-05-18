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
