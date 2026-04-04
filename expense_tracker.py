expenses = []

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    
    expenses.append({"name": name, "amount": amount})
    print("Expense added successfully!\n")

def view_expenses():
    if not expenses:
        print("No expenses recorded.\n")
        return
    
    print("\n--- Expense List ---")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['name']} - ₹{expense['amount']}")
    print()

def total_expense():
    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal Expense: ₹{total}\n")

def main():
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.\n")

main()
