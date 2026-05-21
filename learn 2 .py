expenses = []

while True:
    print("\nExpense tracker")
    print("1. Add an expense")
    print("2. View expenses")
    print("3. Total spend")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Expense name: ")
        try:
            amount = float(input("Amount: "))
        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue
        expense = {"name": name, "amount": amount}
        expenses.append(expense)
        print("Expense added!")

    elif choice == "2":
        print("\nExpenses:")
        if not expenses:
            print("No expenses recorded.")
        for expense in expenses:
            print(f"{expense['name']}: ${expense['amount']}")

    elif choice == "3":
        total = sum(expense["amount"] for expense in expenses)
        print(f"Total expenses: rupees {total}")
        break

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1-4.") 
        
        
    