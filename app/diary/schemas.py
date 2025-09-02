from pydantic import BaseModel


class DiaryBase(BaseModel):
    title: str
    content: str | None
    is_done: bool = False


class DiaryCreate(DiaryBase):
    pass


class DiaryRead(DiaryBase):
    id: int
    # created_at: str

class DiaryUpdate(BaseModel):
    title: str | None = None
    content: str | None = None
