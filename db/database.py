import sqlite3
from datetime import date

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
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS budgets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT NOT NULL,
            amount REAL NOT NULL
        )
    """)
    connection.commit()
    connection.close()

def add_transaction(type, category, amount, description):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
                   INSERT INTO transactions (type, category, amount, description, date)
                   VALUES (?, ?, ?, ?, ?)
    """,            (type, category, float(amount), description, str(date.today())))
    connection.commit()
    connection.close()

def get_all_transactions():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM transactions")
    results = cursor.fetchall()
    connection.close()
    return results

def get_monthly_summary():
    connection = get_connection()
    cursor = connection.cursor()
    current_month = date.today().strftime("%Y-%m")
    cursor.execute("SELECT * FROM transactions WHERE date LIKE ?", (current_month + "%",))
    transactions = cursor.fetchall()
    connection.close()

    income_total = 0
    expense_total = 0
    for transaction in transactions:
        if transaction[1] == "income":
            income_total += transaction[3]
        elif transaction[1] == "expense":
            expense_total += transaction[3]
    return income_total, expense_total

def set_budget(category, amount):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO budgets (category, amount) VALUES (?, ?)", (category, float(amount)))
    connection.commit()
    connection.close()

def get_budget():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM budgets")
    results = cursor.fetchall()
    connection.close()
    return results
