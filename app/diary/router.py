from fastapi import APIRouter
from sqlalchemy import text

from app.core.database import SessionDep
from app.diary.repository import DiaryRepository
from app.diary.schemas import DiaryCreate, DiaryRead

router = APIRouter(prefix="/daily", tags=["daily"])

# @router.get("/")
# async def hello_world():
#     return {
#         "message": "Hello World"
#     }



@router.get("/", response_model=list[DiaryRead])
async def get_all_diaries(session: SessionDep):
    return await DiaryRepository.get_all(session=session)


@router.post("/", response_model=DiaryRead)
async def create_diary(session: SessionDep, data: DiaryCreate,):
    return await DiaryRepository.create(session=session, data=data)



@router.get("/check-db-connection")
async def check_db_connection(session: SessionDep):
    """Check if the database connection is successful"""
    await session.execute(text("SELECT 1"))
    return {"message": "Connection to the database successful"}


