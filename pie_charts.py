#Pie charts done by Lizzy S
import csv
from accounts import create_new_account, view_asset
import matplotlib.pyplot as plt

def pie_charts(expense): #Charts the given data based on expense category into a pie chart
    #Get user data and expense category
    result = get_info
    expense = len(result)
    # Define expense categories by how many values are returned by get_info()
    if expense == 9:
        label = 'Budgeting'
        categories = ['Savings', 'House', 'Utilities', 'Insurance', 'Food', 'Entertainment', 'Healthcare', 'Phone', 'Pet']
        one, two, three, four, five, six, seven, eight, nine = get_info()
        expenses = [one, two, three, four, five, six, seven, eight, nine]
    elif expense == 6:
        label = 'Services'
        categories = ['Utilities' ,'Insurance', 'food', 'Entertainment','Healthcare','Phone']
        one, two, three, four, five, six = get_info()
        expenses = [one, two, three, four, five, six]
    elif expense == 12:
        label = 'All'
        categories = ['Checkings','Salary','Goal','Savings', 'House', 'Utilities', 'Insurance', 'Food', 'Entertainment', 'Healthcare', 'Phone', 'Pet']
        one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve = get_info()
        expenses = [one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve]
    
    # Plotting the pie chart
    fig, ax = plt.subplots()
    ax.pie(expenses, labels=categories, autopct='%1.2f%%') #Makes pie charts and displays the percentages up to the 2nd decimal.
    plt.title(f"Expense: {label}")
    plt.show()


def get_info(): #Gathers info from the user on what kind of things they would like
    found=False
    user = input('What is the name you signed up with, or wish to sign up with?:\n').strip()
    
    # Check if the user already exists in the file
    with open('finacial_data.csv', 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

        # Search for the user
        for row in data:
            try:
                if row[0] == user:
                    found= True
                    password = input("What is your password?:\n") #If the user exists, check password
                    if row[1] == password:
                        print("Login successful!")
                        break
                    else:
                        print("Incorrect password.")
                        return
            except:
                pass
        if found != True: #If the users account isn't found then it will not be marked, 'True'. Also prompts user to create a new account
            print("Account not found.")
            create_account = input("Would you like to create a new account?\n1) Yes\n2) No\n")
            if create_account.lower() == 'yes':
                create_new_account(user)
                get_info()
            elif create_account.lower() == 'no':
                print("Got it. Exiting...\n")
                return
            else:
                print('Please choose a valid answer. (Did you make sure to type in the corresponding number?)\n')
                return
            
    ask = input('Would you like to get a pie chart of your data?\n1) Yes\n2) No\n')
    if ask == '1':
        choice = input('What expense would you like the pie chart for?\n1) Budgeting\n2) Services\n3) ALL\n')
        if choice == '1':
            return [float(i) for i in row[5:13]]
        elif choice == '2':
            return [float(i) for i in row[7:12]]
        elif choice == '3':
            return [float(i) for i in row[2:13]]
        else:
            print('Please choose a valid choice.\n')
            return
    elif ask == '2':
        print('Please choose the corresponding NUMBER.')
        option = input("Got it. Would you like to view a specific assest?\n1) Yes\n2) No\n")
        if option == '1':
            view_asset(row)
        elif option == '2':
            print("Exiting...\n")
            return
        else:
            print('Please choose a valid choice. (Did you make sure to type in the corresponding number?)\n')
            return
    else:
        print('Please choose a valid answer. (Did you make sure to type in the corresponding number?)\n')
        return
