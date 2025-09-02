from fastapi import APIRouter
from sqlalchemy import text

from app.core.database import SessionDep
from app.diary.repository import DiaryRepository
from app.diary.schemas import DiaryCreate, DiaryRead

router = APIRouter(prefix="/daily", tags=["daily"])


@router.get("/", response_model=list[DiaryRead])
async def get_all_diaries(session: SessionDep):
    return await DiaryRepository.get_all(session=session)


@router.post("/", response_model=DiaryRead)
async def create_diary(session: SessionDep, data: DiaryCreate,):
    return await DiaryRepository.create(session=session, data=data)



