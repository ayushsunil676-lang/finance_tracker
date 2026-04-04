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

def add_transaction(type, category, amount, description):
    from datetime import date
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
                   INSERT INTO transactions (type, category, amount, description, date)
                   VALUES (?, ?, ?, ?, ?)
    """,            (type, category, float(amount), description, str(date.today())))
    connection.commit()
    connection.close()