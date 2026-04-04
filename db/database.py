import sqlite3

def get_connection():
    connection = sqlite3.connect("finance.db")
    return connection

def initialize_db():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS transactions  (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   type TEXT NOT NULL,
                   category TEXT NOT NULL,
                   amount REAL NOT NULL,
                   description TEXT,
                   date TEXT NOT NULL
                   )
    """)
    connection.commit()
    connection.close()