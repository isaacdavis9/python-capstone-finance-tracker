def print_welcome():
    print("💰 Welcome to the Personal Finance Tracker!")

def add_expense(expense_data):
    try:
        description = input("Enter expense description: ").strip()
        if not description:
            raise ValueError("Description cannot be empty.")
        
        category = input("Enter category: ").strip().capitalize()
        if not category:
            raise ValueError("Category cannot be empty.")
        
        amount_input = input("Enter amount: ").strip()
        amount = float(amount_input)
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")
        
        expense = (description, amount)
        if category not in expense_data:
            expense_data[category] = []
        expense_data[category].append(expense)
        print("✅ Expense added successfully.")

    except ValueError as ve:
        print(f"❗ {ve}")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")

def view_expenses(expense_data):
    if not expense_data:
        print("📭 No expenses to show.")
        return
    for category, expenses in expense_data.items():
        print(f"\nCategory: {category}")
        for desc, amt in expenses:
            print(f"  - {desc}: ${amt:.2f}")

def view_summary(expense_data):
    if not expense_data:
        print("📭 No data to summarize.")
        return
    print("\n📊 Summary:")
    for category, expenses in expense_data.items():
        total = sum(amount for _, amount in expenses)
        print(f"{category}: ${total:.2f}")

def main():
    expense_data = {}
    print_welcome()

    while True:
        print("\nWhat would you like to do?")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Summary")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense(expense_data)
        elif choice == "2":
            view_expenses(expense_data)
        elif choice == "3":
            view_summary(expense_data)
        elif choice == "4":
            print("👋 Goodbye! Thanks for using the Finance Tracker.")
            break
        else:
            print("❗ Invalid option. Please choose 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
