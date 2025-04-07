# Eli Robison, Goals

import csv

def set_goals():
    try:
        goal_for = input("enter what what you want the name of this goal to be: ")
        goal_is = float(input("enter what you want the goal to be"))
        goal = [goal_for, goal_is, 0]
        with open("my_part/limits.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(goal)
    except:
        print("you must enter a number")
        set_goals()

def advance_goals():
    goals = []

    with open("my_part/limits.csv", "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            goals.append([row[0],row[1],row[2]])

    try:
        wanted_goal_name = input("enter what the name of the goal you want to put money towards: ")
        amount = float(input("enter the amount you want to put towards the goal: "))

        amount = round(amount, 2)
    
        found = 0
        for x in range(len(goals)):
            if wanted_goal_name == goals[x][0]:
                print("you have put $", amount, "towards the", goals[x][0], "goal.")
                found += 1
                break
        if found == 0:
            print("no goal was found with the name", wanted_goal_name)
        
        with open("my_part/goals.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow("")
        for item in goals:
            with open("my_part/goals.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(item)
    except:
        print("you must enter a number")
        advance_goals()

def track_goals():
    goals = []

    with open("my_part/goals.csv", "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            goals.append([row[0],float(row[1]),float(row[2])])
    
    for item in goals:
        gap = item[1] - item[2]
        print("you have $", gap, "left before you reach the", item[0], "goal of", item[1])

def goal_managment():
    choice = input("1. set a savings goal, 2. put money towards a goal or 3. track progress towards a goal? (enter a number): ")
    if choice == "1":
        set_goals()
    elif choice == "2":
        advance_goals()
    elif choice == "3":
        track_goals()
    else:
        print("that is not an option")
        goal_managment()