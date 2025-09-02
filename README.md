# FastAPI Diary — backend (тестовое задание)

Репозиторий: https://github.com/Ridmovies/fastapi-diary-test.

Небольшое асинхронное веб-приложение «ежедневник» (diary) на FastAPI + PostgreSQL. Реализованы все стандартные CRUD-операции и возможность пометить запись выполненной/снять пометку.

## ✨ Функционал
- Создать запись (title, content)
- Прочитать запись по id
- Обновить запись (PATCH)
- Удалить запись
- Просмотреть список записей
- Переключить флаг `is_done` (toggle)

## 🔧 Технологии
- Python 3.12
- FastAPI (async)
- SQLAlchemy 2.0 (async, mapped)
- asyncpg + PostgreSQL
- Docker / docker-compose

---

## Быстрый старт (локально, без Docker)

1. Склонируй репозиторий:
   ```bash
   git clone https://github.com/Ridmovies/fastapi-diary-test.git
   cd fastapi-diary-test
   ```

2. Создай виртуальное окружение и установи зависимости:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. Настрой `.env` (скопируй из `.env.template`), укажи параметры доступа к БД.

4. Запусти приложение (локально):
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   ```

5. Открой Swagger UI: `http://localhost:8000/docs`

---

## Быстрый старт (Docker)

1. Построй и запусти сервисы:
   ```bash
   docker compose up --build
   ```

2. Swagger: `http://localhost:8000/docs`

