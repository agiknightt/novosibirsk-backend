import psycopg2
from fastapi import FastAPI
from config import DB_PASSWORD

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/users")
def get_users_from_db():
    conn = psycopg2.connect(
        dbname="detective_db", 
        user="postgres", 
        password=DB_PASSWORD,  # Используем его тут
        host="localhost"
    )
    
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    result = []
    for row in rows:
        result.append({"id": row[0], "name": row[1], "city": row[2]})

    cursor.close()
    conn.close()

    return result

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"id": user_id, "name": "Пользователь с ID " + str(user_id)}

@app.get("/orders")
async def get_orders():
    return [{"order_id": 1, "amount": 500},
            {"order_id": 2, "amount": 300}]