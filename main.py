import json
# import os
# import tkinter as tk
# from tkinter import messagebox
from datetime import datetime

FILENAME = "expenses.json"

def load_expenses():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_expenses(expenses):
    with open(FILENAME, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expenses():
    amount = float(input("Enter amount: ₹"))
    category = input("Enter Enter category (e.g. food, travel): ")
    note = input("Enter a note (optional): ")
    date = datetime.now().strftime("%Y-%m-%d   %H:%M:%S")

    expense = {
        "amount": amount,
        "category": category,
        "note": note,
        "date": date
    }

    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)

    print("✅ Expense added successfully!")

def total_expenditure():
    exp = load_expenses()
    total = 0
    for item in exp:
        total += item["amount"]
    return total

def filter_expenses():
    exp = load_expenses()
    start_date = input("Enter Start date(YYYY-MM-DD) : ")
    end_date = input("Enter End date(YYYY-MM-DD) : ")
    try:
        start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return
    print(f"\nExpenses from {start_date} to {end_date}:\n")
    found = False
    for item in exp:
        exp_date = item["date"].split()[0]
        exp_date = datetime.strptime(exp_date, "%Y-%m-%d").date()
        if start_date<=exp_date<=end_date :
            print(f"{item['date']} | ₹{item['amount']} | {item['category']} - {item['note']}")
            found = True
    if not found:
        print("No expenses found in this range.")


def main():
    while True:
        print("\n----------Expense Tracker----------")
        print("Choices: ")
        print("0. Exit")
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. Filter View By Date")
        choice = input("Enter Your Choice: ")

        if choice=="1":
            add_expenses()
        elif choice=="2":
            for expence in load_expenses():
                print(f"{expence['date']} | ₹{expence['amount']} | {expence['category']} - {expence['note']}")
        elif choice=="3":
            filter_expenses()
        elif choice=="0":
            print("Total expenditure : ",total_expenditure())
            print("Exiting...")
            break
        else:
            print("!Invalid Choice Please Try Again.")

if __name__ == "__main__":
    main()