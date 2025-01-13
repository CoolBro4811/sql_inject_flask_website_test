import sqlite3

def create_db():
    conn = sqlite3.connect('vulnerable.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL,
                        password TEXT NOT NULL)''')
    # Insert a test user
    cursor.execute('''INSERT INTO users (username, password) VALUES (?, ?)''', ("admin", "password123"))
    conn.commit()
    conn.close()

create_db()

