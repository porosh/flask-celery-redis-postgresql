import os
import psycopg2

# Database configuration
DB_HOST = os.getenv('DB_HOST', 'db')
DB_PORT = os.getenv('DB_PORT', '5432')
DB_NAME = os.getenv('POSTGRES_DB', 'mydatabase')
DB_USER = os.getenv('POSTGRES_USER', 'myuser')
DB_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'mypassword')

def initialize_database():
    conn = psycopg2.connect(host=DB_HOST, port=DB_PORT, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (id SERIAL PRIMARY KEY, name TEXT)''')
    conn.commit()
    conn.close()

def insert_data_to_db():
    conn = psycopg2.connect(host=DB_HOST, port=DB_PORT, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
    c = conn.cursor()
    c.execute("INSERT INTO tasks (name) VALUES ('Short task')")
    conn.commit()
    conn.close()
    return 'Data inserted into database'

def insert_task(name):
    conn = psycopg2.connect(host=DB_HOST, port=DB_PORT, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
    c = conn.cursor()
    c.execute("INSERT INTO tasks (name) VALUES (%s)", (name,))
    conn.commit()
    conn.close()

def get_task(task_id):
    conn = psycopg2.connect(host=DB_HOST, port=DB_PORT, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
    c = conn.cursor()
    c.execute("SELECT * FROM tasks WHERE id=%s", (task_id,))
    task = c.fetchone()
    conn.close()
    return task

def get_all_tasks():
    conn = psycopg2.connect(host=DB_HOST, port=DB_PORT, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()
    conn.close()
    return tasks

def update_task(task_id, name):
    conn = psycopg2.connect(host=DB_HOST, port=DB_PORT, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
    c = conn.cursor()
    c.execute("UPDATE tasks SET name=%s WHERE id=%s", (name, task_id))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = psycopg2.connect(host=DB_HOST, port=DB_PORT, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
    c = conn.cursor()
    c.execute("DELETE FROM tasks WHERE id=%s", (task_id,))
    conn.commit()
    conn.close()
