from fastapi import FastAPI
import mysql.connector

app = FastAPI()

@app.get("/{user_id}")
def read_user(user_id: int):
    conn = mysql.connector.connect(host="db", user="root", password="rootpass", database="crud_db")
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result or {"message": "User not found"}

