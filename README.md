# 💰 Personal Finance Tracker

A CLI-based personal finance tracker built with Python and SQLite.
Track your income, expenses, and budgets — all from the terminal.

## Features

- Add income and expenses with categories
- View all transactions in a clean format
- Monthly summary with total income, expenses, and balance
- Budget management with overspending warnings

## Tech Stack

- Python 3
- SQLite3 (built-in, no installation needed)
- CLI interface

## Project Structure

```text
finance_tracker/
├── main.py              # Entry point
├── cli/
│   └── menu.py          # User interface and input
├── db/
│   └── database.py      # Database logic
├── models/              # For future data models
├── services/            # For future business logic
└── requirements.txt
```

## How to Run

```bash
git clone https://github.com/ayushsunil676-lang/finance_tracker.git
cd finance_tracker
python3 main.py
```

## Usage

| Option | Description |
|--------|-------------|
| 1 | Add a new transaction |
| 2 | View all transactions |
| 3 | View monthly summary |
| 4 | Manage budgets |
| 5 | Exit |

