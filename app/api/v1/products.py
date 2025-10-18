from fastapi import APIRouter, Depends
from app.api.v1.auth import get_current_user

router = APIRouter()

# Public endpoint
@router.get("/ping", summary="Ping products")
async def ping_products():
    return {"message": "Products router works"}

# Protected endpoint
@router.get("/", summary="Get all products")
async def list_products(current_user: dict = Depends(get_current_user)):
    return [
        {"id": 1, "name": "Laptop"},
        {"id": 2, "name": "Phone"}
    ]
