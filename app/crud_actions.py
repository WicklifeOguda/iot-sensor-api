from sqlalchemy.orm import Session

from . import models, schemas

"""
Isolated action fuctions for saving and fetching records to and from the databse
"""


def save_reading(db: Session, reading: schemas.IncomingSensorData):
    db_reading = models.SensorReading(**reading.model_dump())
    db.add(db_reading)
    db.commit()
    db.refresh(db_reading)
    return db_reading


def fetch_readings(db: Session, device_id: str, limit: int = 10):
    return (
        db.query(models.SensorReading)
        .filter(models.SensorReading.device_id == device_id)
        .order_by(models.SensorReading.timestamp.desc())
        .limit(limit)
        .all()
    )
