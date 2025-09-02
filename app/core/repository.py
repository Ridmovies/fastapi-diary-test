from pydantic import BaseModel
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
        """Получить все записи из таблицы"""
        query = select(cls.model)
        result = await session.execute(query)
        return result.scalars().all()

    @classmethod
    async def get_by_id(cls, session: AsyncSession, model_id: int):
        query = select(cls.model).filter_by(id=int(model_id))
        result = await session.execute(query)
        return result.scalar_one_or_none()


    @classmethod
    async def create(cls, session: AsyncSession, data: BaseModel ):
        """Создать новую запись"""
        # Преобразуем Pydantic модель в словарь, если это Pydantic модель
        data_dict = data.model_dump(exclude_unset=True, exclude_none=True)

        instance = cls.model(**data_dict)  # Распаковываем словарь в аргументы конструктора модели
        session.add(instance)
        await session.commit()
        return instance

    @classmethod
    async def delete(cls, session: AsyncSession, model_id: int):
        if model_id:
            query = select(cls.model).filter_by(id=model_id)
            result = await session.execute(query)
            instance = result.scalar_one_or_none()
            if instance:
                await session.delete(instance)
                await session.commit()




