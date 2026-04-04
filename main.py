from cli.menu import show_main_menu

while True:
    choice = show_main_menu()
    if choice == "1":
        print("TODO: Add Transaction")
    elif choice == "2":
        print("TODO: View Transactions")
    elif choice == "3":
        print("TODO: Monthly Summary")
    elif choice == "4":
        print("TODO: Manage Budgets")
    elif choice == "5":
        print("Goodbye!")
        break