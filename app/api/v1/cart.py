from fastapi import APIRouter, Depends
from app.api.v1.auth import get_current_user

router = APIRouter()

@router.get("/ping", summary="Ping orders")
async def ping_orders():
    return {"message": "Orders router works"}

@router.get("/", summary="Get user orders")
async def get_orders(current_user: dict = Depends(get_current_user)):
    user_id = current_user["id"]
    return {"user_id": user_id, "orders": []}  # example empty orders
