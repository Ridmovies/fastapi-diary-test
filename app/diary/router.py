from fastapi import APIRouter
from sqlalchemy import text

from app.core.database import SessionDep

router = APIRouter(prefix="/daily", tags=["daily"])

@router.get("/")
async def hello_world():
    return {
        "message": "Hello World"
    }


@router.get("/check-db-connection")
async def check_db_connection(session: SessionDep):
    """Check if the database connection is successful"""
    await session.execute(text("SELECT 1"))
    return {"message": "Connection to the database successful"}