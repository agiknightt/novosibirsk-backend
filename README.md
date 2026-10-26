# novosibirsk-backend
First FastAPI project: connects to PostgreSQL and returns users/orders

```markdown
# Detective API (FastAPI + PostgreSQL)

Мой первый backend-проект на Python. API для работы с базой данных интернет-магазина.

## 🚀 Технологии
- Python 3
- FastAPI (веб-фреймворк)
- PostgreSQL (база данных)
- psycopg2 (драйвер для подключения к БД)

## 📡 Эндпоинты
- `GET /users` — вернуть список всех пользователей из базы
- `GET /users/{id}` — вернуть пользователя по ID
- `GET /orders` — вернуть список заказов

## ⚙️ Как запустить
1. Установите зависимости:
   ```bash
   pip install fastapi uvicorn psycopg2-binary
```

2. Создайте базу данных detective_db в PostgreSQL и таблицы (SQL-скрипт в файле init.sql).
3. Запустите сервер:
   ```bash
   uvicorn main:app --reload
   ```
4. Откройте в браузере: http://127.0.0.1:8000/docs
