from cli.menu import show_main_menu
from db.database import initialize_db 
from cli.menu import get_transaction_input
from db.database import add_transaction
from db.database import get_all_transactions
from db.database import get_monthly_summary
from db.database import set_budget
from db.database import get_budget

initialize_db()

while True:
    choice = show_main_menu()
    if choice == "1":
        type, category, amount, description = get_transaction_input()
        add_transaction(type, category, amount, description)
        print("✅ Transaction saved!")
    elif choice == "2":
        transactions = get_all_transactions()
        for transaction in transactions:
            print(f"[{transaction[0]}] {transaction[5]} | {transaction[1]} | {transaction[2]} | €{transaction[3]} | {transaction[4]}")
    elif choice == "3":
        income, expenses = get_monthly_summary()
        balance = income - expenses
        print(f"--- Monthly Summary ---")
        print(f"Total Income:   €{income}")
        print(f"Total Expenses: €{expenses}")
        print(f"Balance:        €{balance}")
    elif choice == "4":
        print("1. Set Budget")
        print("2. View Budgets")
        budget_choice = input("Enter choice: ")
    if budget_choice == "1":
            category = input("Category: ")
            amount = input("Budget amount: ")
            set_budget(category, amount)
            print(f"✅ Budget set for {category}: €{amount}")
    elif budget_choice == "2":
            budgets = get_budget()
            for budget in budgets:
                print(f"{budget[1]}: €{budget[2]}")
    elif choice == "5":
        print("Goodbye!")
        break