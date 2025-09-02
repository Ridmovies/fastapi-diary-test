from fastapi import APIRouter


router = APIRouter(prefix="/daily", tags=["daily"])

@router.get("/")
async def hello_world():
    return {
        "message": "Hello World"
    }
