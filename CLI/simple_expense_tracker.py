expenses = []

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        expenses.append(amount)
        print("Expense added")

    elif choice == "2":
        if not expenses:
            print("No expenses")
        else:
            for i in range(len(expenses)):
                print(i + 1, "-", expenses[i])

    elif choice == "3":
        print("Total:", sum(expenses))

    elif choice == "4":
        break

    else:
        print("Invalid choice")
