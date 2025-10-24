from fastapi import FastAPI
import mysql.connector
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    email: str

@app.put("/{user_id}")
def update_user(user_id: int, user: User):
    conn = mysql.connector.connect(host="db", user="root", password="rootpass", database="crud_db")
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name = %s, email = %s WHERE id = %s", (user.name, user.email, user_id))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "User updated"}

