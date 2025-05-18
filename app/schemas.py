from datetime import datetime

from pydantic import BaseModel, Field


class IncomingSensorData(BaseModel):
    """
    Validation schema for sensor data received by the API
    """

    device_id: str
    temperature: float = Field(..., ge=-50, le=150)
    humidity: float = Field(..., ge=0, le=100)
    timestamp: datetime


class OutgoingSensorData(IncomingSensorData):
    """
    Validation schema for sensor data sent by the API
    """

    id: int

    class ConfigDict:
        orm_mode = True
