from fastapi import APIRouter

from app.core.database import SessionDep
from app.diary.repository import DiaryRepository
from app.diary.schemas import DiaryCreate, DiaryRead

router = APIRouter(prefix="/daily", tags=["daily"])


@router.get("/", response_model=list[DiaryRead])
async def get_all_diaries(session: SessionDep):
    return await DiaryRepository.get_all(session=session)


@router.get("/{diary_id}", response_model=DiaryRead)
async def get_diary_by_id(session: SessionDep, diary_id: int):
    return await DiaryRepository.get_by_id(session=session, model_id=diary_id)


@router.post("/", response_model=DiaryRead)
async def create_diary(session: SessionDep, data: DiaryCreate,):
    return await DiaryRepository.create(session=session, data=data)
