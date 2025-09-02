from fastapi import FastAPI

from app.diary.router import router as diary_router


app = FastAPI()



app.include_router(diary_router)

