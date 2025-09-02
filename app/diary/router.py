from fastapi import APIRouter
from starlette.status import HTTP_204_NO_CONTENT

from app.core.database import SessionDep
from app.diary.repository import DiaryRepository
from app.diary.schemas import DiaryCreate, DiaryRead, DiaryUpdate

router = APIRouter(prefix="/api/daily", tags=["daily"])


@router.get("/", response_model=list[DiaryRead])
async def get_all_diaries(session: SessionDep):
    return await DiaryRepository.get_all(session=session)


@router.get("/{diary_id}", response_model=DiaryRead)
async def get_diary_by_id(session: SessionDep, diary_id: int):
    return await DiaryRepository.get_by_id(session=session, model_id=diary_id)


@router.post("/", response_model=DiaryRead)
async def create_diary(session: SessionDep, data: DiaryCreate,):
    return await DiaryRepository.create(session=session, data=data)


@router.delete("/{diary_id}", status_code=HTTP_204_NO_CONTENT)
async def delete_diary(session: SessionDep, diary_id: int):
    await DiaryRepository.delete(session=session, model_id=diary_id)
    return


@router.patch("/{diary_id}", response_model=DiaryRead)
async def update_diary(session: SessionDep, diary_id: int, data: DiaryUpdate):
    return await DiaryRepository.patch(session=session, data=data, model_id=diary_id)


@router.post("/{diary_id}/done", response_model=DiaryRead)
async def done_diary(session: SessionDep, diary_id: int):
    return await DiaryRepository.done(session=session, diary_id=diary_id)
