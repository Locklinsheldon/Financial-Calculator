# Eli Robison, Goals

# statment that lets csv files work
import csv

# function that lets the user make a new goal
def set_goals():
    try:
        goal_for = input("enter what what you want the name of this goal to be: ")
        goal_is = float(input("enter how much you want the goal to be: "))
        goal = [goal_for, goal_is, 0]
        with open("goals.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(goal)
    except:
        print("you must enter a number")
        # statment that makes it so the code runs again if an error happens
        set_goals()

# function that lets the user put money towards a goal
def advance_goals():
    goals = []

    with open("goals.csv", "r") as file:
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
                goals[x][2] = float(goals[x][2]) + amount
                print("you have put $", amount, "towards the", goals[x][0], "goal.")
                found += 1
        if found == 0:
            print("no goal was found with the name", wanted_goal_name)
        
        count = 0

        for item in goals:
            if count == 0:
                with open("goals.csv", "w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(item)
                    count += 1
            else:
                with open("goals.csv", "a", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(item)
    except:
        print("you must enter a number")
        # statment that makes it so the code runs again if an error happens
        advance_goals()

# function that lets the user track how much is left before they reach their goals
def track_goals():
    goals = []

    with open("goals.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            goals.append([row[0],float(row[1]),float(row[2])])
    
    for item in goals:
        gap = item[1] - item[2]
        print("you have $", gap, "left before you reach the", item[0], "goal of $", item[1])

# function that lets the user choose what they want to do
def goal_managment():
    # loop that makes sure the program continues until the user is done
    while True:
        choice = input("Which one would you like to do?:\n\n1. set a savings goal\n2. put money towards a goal\n3. track progress towards a goal?\n4. Go back\n\n(enter a number): ")
        if choice == "1":
            set_goals()
        elif choice == "2":
            advance_goals()
        elif choice == "3":
            track_goals()
        elif choice == '4':
            break
        else:
            print("that is not an option")
            # statment that makes it so the code goes to the next iteration if the use enters something that is not an option
            continue