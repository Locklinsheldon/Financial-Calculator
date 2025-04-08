#Finacial project Lizzy Saldana

import time
import csv

def view_asset(row): #Allows the user to pick a row and view the assest they would like to.
    assets = {
        "Checkings": row[2],
        "Salary": row[3],
        "Goal": row[4],
        "Savings": row[5],
        "House": row[6],
        "Utilities": row[7],
        "Insurance": row[8],
        "Food": row[9],
        "Entertainment": row[10],
        "Healthcare": row[11],
        "Phone": row[12],
        "Pet": row[13]
    }
    print("\nHere are your available assets to choose from.\n---------------\n") 
    asset_names = input('1) checkings\n2) salary\n3) goal\n4) savings\n5) house\n6) utilities\n7) insurance\n8) food\n9) entertainment\n10) healthcare\n11) phone\n12) pet\n13) all\n')
    if asset_names == '1':
        print(f"Checkings: ${assets['Checkings']}\n")
    elif asset_names == '2':
        print(f"Salary: ${assets['Salary']}\n")
    elif asset_names == '3':
        print(f"Goal: ${assets['Goal']}\n")
    elif asset_names == '4':
        print(f"Savings: ${assets['Savings']}\n")
    elif asset_names == '5':
        print(f"House: ${assets['House']}\n")
    elif asset_names == '6':
        print(f"Utilities: ${assets['Utilities']}\n")
    elif asset_names == '7':
        print(f"Insurance: ${assets['Insurance']}\n")
    elif asset_names == '8':
        print(f"Food: ${assets['Food']}\n")
    elif asset_names == '9':
        print(f"Entertainment: ${assets['Entertainment']}\n")
    elif asset_names == '10':
        print(f"Healthcare: ${assets['Healthcare']}\n")
    elif asset_names == '11':
        print(f"Phone: ${assets['Phone']}\n")
    elif asset_names == '12':
        print(f"Pet: ${assets['Pet']}\n")
    elif asset_names == '13':
        print('--------------')
        for asset, value in assets.items(): #Prints all of the assets
            print(f"{asset}: ${value}")
    else:
        print("Please choose a valid input. (Make sure you are picking the corresponding numbers)")
    time.sleep(2) #Pauses code executing for 2 seconds
    return



def create_new_account(user): #Creates new account for the user
    try:
        password = input("Enter your new password: ")
        checkings = float(input("How much is in your checkings account right now?:\n"))
        salary = float(input('How much do you make per year?:\n'))
        goal = float(input("What is your GOAL? (If you don't have one, input 0):\n"))
        savings = float(input("How much do you have in SAVINGS? (If you don't have any, input 0):\n"))
        house = float(input("How much money do you spend on HOUSE fees every year?:\n"))
        utilities = float(input("How much do you spend on UTILITIES every year?:\n"))
        insurance = float(input("How much do you spend on INSURANCE every year?:\n"))
        food = float(input("How much do you spend on FOOD per year?:\n"))
        entertainment = float(input("How much do you spend on ENTERTAINMENT per year?:\n"))
        healthcare = float(input("How much do you spend on HEALTHCARE every year?:\n"))
        phone = float(input("What is your PHONE bill per year?:\n"))
        pet = float(input("How much do you spend on PET related items per year?:\n"))
    except:
        print("Please pick valid numbers!! ")
        return

    with open('finacial_data.csv', 'a') as file: #Use a instead of w so it doesn't delete all of our data
        writer = csv.writer(file)
        writer.writerow([user, password, checkings, salary, goal, savings, house, utilities, insurance, food, entertainment, healthcare, phone, pet])

    print('account created!\n')
    return