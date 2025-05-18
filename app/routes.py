from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def check_api_health():
    return {"status": "OK"}
