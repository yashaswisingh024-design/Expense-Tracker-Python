import os

expenses = []

# Load data from file
def load_expenses():
    if os.path.exists("expenses.txt"):
        with open("expenses.txt", "r") as file:
            for line in file:
                name, amount = line.strip().split(",")
                expenses.append({"name": name, "amount": float(amount)})

# Save data to file
def save_expense(name, amount):
    with open("expenses.txt", "a") as file:
        file.write(f"{name},{amount}\n")

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    
    expenses.append({"name": name, "amount": amount})
    save_expense(name, amount)
    
    print("Expense added & saved!\n")

def view_expenses():
    if not expenses:
        print("No expenses found.\n")
        return
    
    print("\n--- Expenses ---")
    for e in expenses:
        print(f"{e['name']} - ₹{e['amount']}")
    print()

def total_expense():
    total = sum(e["amount"] for e in expenses)
    print(f"\nTotal Expense: ₹{total}\n")

def main():
    load_expenses()  # load on start

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
            print("Invalid choice\n")

main()
