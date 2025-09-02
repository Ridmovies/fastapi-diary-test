from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.database import init_db
from app.diary.router import router as diary_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Обновление БД...")
    await init_db()
    yield
    # Здесь можно что-то выполнить при завершении работы


app = FastAPI(lifespan=lifespan)


app.include_router(diary_router)

