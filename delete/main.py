from fastapi import FastAPI
import mysql.connector

app = FastAPI()

@app.delete("/{user_id}")
def delete_user(user_id: int):
    conn = mysql.connector.connect(host="db", user="root", password="rootpass", database="crud_db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "User deleted"}

