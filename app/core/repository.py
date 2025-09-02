from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class BaseRepository:
    """Базовый репозиторий для CRUD операций с моделями SQLAlchemy.

    Attributes:
        model: Модель SQLAlchemy, с которой работает репозиторий
               (должен быть переопределен в дочерних классах)
    """
    model = None


    @classmethod
    async def get_all(cls, session: AsyncSession):
        query = select(cls.model)
        result = await session.execute(query)
        return result.scalars().all()




