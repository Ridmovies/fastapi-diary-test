from fastapi import APIRouter
from sqlalchemy import text

from app.core.database import SessionDep
from app.diary.repository import DiaryRepository

router = APIRouter(prefix="/daily", tags=["daily"])

# @router.get("/")
# async def hello_world():
#     return {
#         "message": "Hello World"
#     }



@router.get("/")
async def get_all_diaries(session: SessionDep):
    return await DiaryRepository.get_all(session=session)




@router.get("/check-db-connection")
async def check_db_connection(session: SessionDep):
    """Check if the database connection is successful"""
    await session.execute(text("SELECT 1"))
    return {"message": "Connection to the database successful"}


