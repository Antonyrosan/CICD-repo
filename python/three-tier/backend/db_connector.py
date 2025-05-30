import os
import mysql.connector

conn = mysql.connector.connect(
    host=os.getenv('DB_HOST', 'localhost'),
    user=os.getenv('DB_USER', 'root'),
    password=os.getenv('DB_PASSWORD', ''),
    database=os.getenv('DB_NAME', 'studentdb')
)

print("Connected successfully")
conn.close()
def connect_db():
    return mysql.connector.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        user=os.getenv('DB_USER', 'root'),
        password=os.getenv('DB_PASSWORD', ''),
        database=os.getenv('DB_NAME', 'studentdb')
    )

def get_all_students():
    conn = connect_db()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM students")
    students = cur.fetchall()
    cur.close()
    conn.close()
    return students

def add_student(name, age, department):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO students (name, age, department) VALUES (%s, %s, %s)",
        (name, age, department)
    )
    conn.commit()
    cur.close()
    conn.close()

def update_student(id, name, age, department):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(
        "UPDATE students SET name=%s, age=%s, department=%s WHERE id=%s",
        (name, age, department, id)
    )
    conn.commit()
    cur.close()
    conn.close()

def delete_student(id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE id=%s", (id,))
    conn.commit()
    cur.close()
    conn.close()
