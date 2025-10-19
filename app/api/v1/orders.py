from fastapi import APIRouter

router = APIRouter()

@router.get("/ping", summary="Ping orders")
async def ping_orders():
    return {"message": "Orders router works"}
