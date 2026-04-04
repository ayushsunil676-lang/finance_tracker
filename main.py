from cli.menu import show_main_menu
from db.database import initialize_db 
from cli.menu import get_transaction_input
from db.database import add_transaction

initialize_db()

while True:
    choice = show_main_menu()
    if choice == "1":
        type, category, amount, description = get_transaction_input()
        add_transaction(type, category, amount, description)
        print("✅ Transaction saved!")
    elif choice == "2":
        print("TODO: View Transactions")
    elif choice == "3":
        print("TODO: Monthly Summary")
    elif choice == "4":
        print("TODO: Manage Budgets")
    elif choice == "5":
        print("Goodbye!")
        break