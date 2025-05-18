from fastapi import APIRouter

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
