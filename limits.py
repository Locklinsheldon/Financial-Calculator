# Eli Robison, Limits

import csv

def set_limits():
    try:
        num_limits = int(input("enter the number of limits you want to set: "))
        for x in range(num_limits):
            limit_for = input("enter what expence this limit is for: ")
            limit_is = int(input("enter what you want the limit to be"))
            with open("my_part/limits.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(limit_for, limit_is)
    except:
        print("you must enter a number")
        set_limits()

def compare_limits():
    limits = []

    with open("my_part/limits.csv", "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            limits.append([row[0],row[1]])
    
    expenses = []

    with open("my_part/expenses.csv", "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            expenses.append([row[0],row[1]])
    
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

def limit_managment():
    choice = input("1. set budget limit or 2. compare expenses? (enter a number): ")
    if choice == "1":
        set_limits()
    elif choice == "2":
        compare_limits()
    else:
        print("that is not an option")
        limit_managment()