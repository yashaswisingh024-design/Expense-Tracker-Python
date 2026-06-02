import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os

FILE_NAME = "expenses.csv"

expenses = []


def load_expenses():
    expenses.clear()

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)

            for row in reader:
                if len(row) == 2:
                    try:
                        expenses.append({
                            "name": row[0],
                            "amount": float(row[1])
                        })
                    except ValueError:
                        pass


def save_all_expenses():
    with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        for expense in expenses:
            writer.writerow([
                expense["name"],
                expense["amount"]
            ])


def update_total():
    total = sum(expense["amount"] for expense in expenses)
    total_label.config(text=f"Total Expense: ₹{total:.2f}")


def refresh_table():
    for item in tree.get_children():
        tree.delete(item)

    for expense in expenses:
        tree.insert(
            "",
            "end",
            values=(
                expense["name"],
                f"₹{expense['amount']:.2f}"
            )
        )

    update_total()


def add_expense():
    name = name_entry.get().strip()
    amount_text = amount_entry.get().strip()

    if not name:
        messagebox.showerror("Error", "Enter expense name")
        return

    try:
        amount = float(amount_text)

        if amount <= 0:
            raise ValueError

    except ValueError:
        messagebox.showerror(
            "Error",
            "Enter a valid amount"
        )
        return

    expenses.append({
        "name": name,
        "amount": amount
    })

    save_all_expenses()
    refresh_table()

    name_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)

    name_entry.focus()


def delete_expense():
    selected = tree.selection()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Select an expense to delete"
        )
        return

    index = tree.index(selected[0])

    del expenses[index]

    save_all_expenses()
    refresh_table()


# ------------------ UI ------------------

root = tk.Tk()
root.title("Expense Tracker")
root.geometry("700x500")
root.resizable(False, False)

title = tk.Label(
    root,
    text="Expense Tracker",
    font=("Arial", 20, "bold")
)
title.pack(pady=15)

input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(
    input_frame,
    text="Expense Name"
).grid(row=0, column=0, padx=10)

name_entry = tk.Entry(
    input_frame,
    width=25
)
name_entry.grid(row=0, column=1)

tk.Label(
    input_frame,
    text="Amount (₹)"
).grid(row=0, column=2, padx=10)

amount_entry = tk.Entry(
    input_frame,
    width=15
)
amount_entry.grid(row=0, column=3)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_btn = tk.Button(
    button_frame,
    text="Add Expense",
    width=15,
    command=add_expense
)
add_btn.grid(row=0, column=0, padx=10)

delete_btn = tk.Button(
    button_frame,
    text="Delete Selected",
    width=15,
    command=delete_expense
)
delete_btn.grid(row=0, column=1, padx=10)

columns = ("Expense", "Amount")

tree = ttk.Treeview(
    root,
    columns=columns,
    show="headings",
    height=15
)

tree.heading("Expense", text="Expense")
tree.heading("Amount", text="Amount")

tree.column("Expense", width=400)
tree.column("Amount", width=200)

tree.pack(pady=10)

total_label = tk.Label(
    root,
    text="Total Expense: ₹0.00",
    font=("Arial", 14, "bold")
)

total_label.pack(pady=10)

load_expenses()
refresh_table()

root.mainloop()
