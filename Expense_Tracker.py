import os
import json
from argparse import ArgumentParser

# we are using two main thing
# 1. JSON.dump() to save all our given python data to save into out expenseSheet as a JSON file way
# 2. JSON.load() to read all JSON data in a python way

expenseSheet = 'EXP.txt'
if os.path.exists(expenseSheet):
    with open(expenseSheet, 'r') as file:
        expenses = json.load(file)
        # JSON.load() is used for reading JSON data into Python way
else:
    expenses = []


def save_data():
    with open(expenseSheet, 'w') as file:
        json.dump(expenses, file, indent=4)


def add_expense_data(Product_name, Product_descrip, Product_amount):
    expense = {
        "Product_name": Product_name,
        "Product_descrip": Product_descrip,
        "Product_amount": Product_amount
    }
    expenses.append(expense)
    save_data()
    print("data added...")


def update_expense_data():
    name = input("enter Product Name of update :")
    for expense in expenses:
        if expense["Product_name"] == name:
            expense["Product_descrip"] = input('enter product description :')
            expense["Product_amount"] = int(input("enter product amount :"))
            save_data()

        else:
            print(f"product {name} is not found")


def delete_expense_data():
    name = input("enter Product Name :")
    for expense in expenses:
        if expense["Product_name"] == name:
            expenses.remove(expense)
            print(f"{name} is deleted sucessfully")
            save_data()
        else:
            print(f"prodct {name} deleted sucessfully")


def view_expense_data():
    if expenses:
        for expense in expenses:
            print(
                f"Product_name :{expense['Product_name']}, Product_descrip:{expense['Product_descrip']}, Product_amount :{expense['Product_amount']}")


# view summary of all expenses
def view_expense():
    for expense in expenses:
        print(f"Product_expense :{expense['Product_amount']}")


def main():
    parser = ArgumentParser()
    parser.add_argument("--add", action="store_true", help="adding the data")
    parser.add_argument("--view", action="store_true", help="viewing the data")
    parser.add_argument("--Product_name", type=str,
                        help="enter the product name")
    parser.add_argument("--Product_descrip", type=str,
                        help="entring the discription of the product")
    parser.add_argument("--Product_amount", type=int,
                        help="enter the amount of the product")
    parser.add_argument("--update", action="store_true",
                        help="updating the data")
    parser.add_argument("--delete", action="store_true",
                        help="delete the product")
    parser.add_argument("--view_expense", action="store_true",
                        help="viewing the expense summary")

    args = parser.parse_args()

    if (args.add) and (args.Product_name) and (args.Product_descrip) and (args.Product_amount):
        add_expense_data(args.Product_name,
                         args.Product_descrip, args.Product_amount)
    elif (args.view):
        view_expense_data()
    elif (args.update):
        update_expense_data()
    elif (args.delete):
        delete_expense_data()
    elif (args.view_expense):
        view_expense()
    else:
        print(parser.print_help())


if __name__ == "__main__":
    main()
