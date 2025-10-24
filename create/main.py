from fastapi import FastAPI
import mysql.connector
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    email: str

@app.post("/")
def create_user(user: User):
    conn = mysql.connector.connect(host="db", user="root", password="rootpass", database="crud_db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (user.name, user.email))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "User created"}

