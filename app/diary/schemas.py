from pydantic import BaseModel


class DiaryBase(BaseModel):
    title: str
    content: str | None


class DiaryCreate(DiaryBase):
    pass


class DiaryRead(DiaryBase):
    id: int
    # created_at: str