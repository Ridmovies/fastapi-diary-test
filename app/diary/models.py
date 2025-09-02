from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Diary(Base):
    __tablename__ = "diary"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    content: Mapped[str | None]
    is_done: Mapped[bool] = mapped_column(default=False)