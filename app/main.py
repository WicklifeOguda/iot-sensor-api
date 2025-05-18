from fastapi import FastAPI

from . import models, routes
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="IoT Sensor API")

app.include_router(routes.router)
