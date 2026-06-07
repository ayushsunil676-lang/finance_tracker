def show_main_menu():
    print("---Personal Finance Tracker---")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. Monthly Summary")
    print("4. Manage Budgets")
    print("5. Exit")
    print("6. Delete Transaction")
    choice = input("Enter your choice:")
    return choice

def get_transaction_input():
    type = input("Type (income/expense): ")
    if type == "income":
        category = input("Source (Salary/Freelance/Gift/Tips/Other): ")
    else:
        category = input("Category (Food/Rent/Transport/Groceries/Misc.): ")
    amount = input("Amount: ")
    description = input("Description: ")
    return type, category, amount, description