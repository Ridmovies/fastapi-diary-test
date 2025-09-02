# Определяем параметры подключения к БД в зависимости от режима работы (тестовый/обычный)
from typing import AsyncGenerator, Annotated

from fastapi import Depends
from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs, AsyncSession
from sqlalchemy.orm import DeclarativeBase

from app.core.config import settings

if settings.MODE == "TEST":
    DATABASE_URL = settings.TEST_DB_URL  # URL тестовой БД
    DATABASE_PARAMS = {"poolclass": NullPool}  # Отключаем пул соединений для тестов
else:
    DATABASE_URL = settings.DATABASE_URL  # URL основной БД
    DATABASE_PARAMS = {}  # Используем стандартный пул соединений

# Создаем асинхронный движок SQLAlchemy:
# - echo=False - отключаем логирование SQL-запросов
# - **DATABASE_PARAMS - передаем дополнительные параметры
engine = create_async_engine(DATABASE_URL, echo=False, **DATABASE_PARAMS)

# Создаем фабрику асинхронных сессий:
# - expire_on_commit=False - отключаем автоматическое истечение сессии после коммита
async_session = async_sessionmaker(engine, expire_on_commit=False)


# Базовый класс для всех SQLAlchemy моделей
class Base(AsyncAttrs, DeclarativeBase):
    pass


# Асинхронный генератор для получения сессии БД
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:  # Создаем новую сессию
        yield session  # Возвращаем сессию через yield (паттерн dependency injection)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


# Тип-алиас для аннотаций зависимостей FastAPI:
# Позволяет использовать SessionDep в параметрах роутов вместо явного Depends(get_session)
SessionDep:  type[AsyncSession] = Annotated[AsyncSession, Depends(get_session)]