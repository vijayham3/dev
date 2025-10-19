from fastapi import APIRouter

# Create the router instance
router = APIRouter()

# Example endpoint to test router
@router.get("/ping", summary="Ping auth router")
async def ping_auth():
    return {"message": "Auth router works"}
