from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.repository import BaseRepository
from app.diary.models import Diary


class DiaryRepository(BaseRepository):
    model = Diary

    @classmethod
    async def done(cls, diary_id: int, session: AsyncSession) -> Diary | None:
        """ Переключаем статус записи на противоположный """
        query = select(cls.model).filter_by(id=diary_id)
        result = await session.execute(query)
        diary: Diary = result.scalar_one_or_none()

        if not diary:
            return None

        diary.is_done = not diary.is_done
        await session.commit()
        return diary
