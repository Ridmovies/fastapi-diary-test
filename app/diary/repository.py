from app.core.repository import BaseRepository
from app.diary.models import Diary


class DiaryRepository(BaseRepository):
    model = Diary