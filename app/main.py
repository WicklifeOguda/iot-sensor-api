from fastapi import FastAPI
from . import routes

app = FastAPI(title="IoT Sensor API")

app.include_router(routes.router)
