from sqlalchemy import Column, DateTime, Float, Integer, String

from .database import Base


class SensorReading(Base):
    """
    Holds the data received from the sensor readings
    """

    __tablename__ = "sensor_readings"

    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(String, index=True)
    temperature = Column(Float)
    humidity = Column(Float)
    timestamp = Column(DateTime)
