# Eli Robison, Limits

# statment that lets csv files work
import csv

# function that lets the user set new limits
def set_limits():
    try:
        num_limits = int(input("enter the number of limits you want to set: "))
        for x in range(num_limits):
            limit_for = input("enter what expence this limit is for: ")
            limit_is = float(input("enter what you want the limit to be: "))
            limit = [limit_for,limit_is]
            with open("limits.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(limit)
    except:
        print("you must enter a number")
        # statment that makes it so the code runs again if an error happens
        set_limits()

# function that lets the user compare limits to the assosiated expense
def compare_limits():
    limits = []

    with open("limits.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            limits.append([row[0],float(row[1])])
    
    expenses = []

    with open("expenses.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            expenses.append([row[0],float(row[1])])
    
    for limit in limits:
        found = 0
        for item in expenses:
            if limit[0] == item[0]:
                gap = limit[1] - item[1]
                print("you have $", gap, "left before you reach the", limit[0], "limit.")
                found += 1
                break
        if found == 0:
            print("no expense was associated with the", limit, "limit.")

# function that lets the user set expenses to compare
def expense_managment():
    try:
        expense_for = input("enter what this expense is for: ")
        expense_is = float(input("enter how much the expense is: "))
        expense = [expense_for, expense_is]
        with open("expenses.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(expense)
    except:
        print("you must enter a number")
        # statment that makes it so the code runs again if an error happens
        expense_managment()

# function that lets the user choose what they want to do
def limit_managment():
    # loop that makes sure the program continues until the user is done
    while True:
        choice = input("Which one would you like to do?:\n\n1. set budget limit\n2. compare expenses\n3. add an expense to be compared?\n4. Go back\n\n(enter a number): ")
        if choice == "1":
            set_limits()
        elif choice == "2":
            compare_limits()
        elif choice == "3":
            expense_managment()
        elif choice == '4':
            break
        else:
            print("that is not an option")
            # statment that makes it so the code goes to the next iteration if the use enters something that is not an option
            continue