#Financial info main, Connor Pavicic

from income import income
from expense import expense
from display_info import display_csv
from view_money_time_period import view_money_history

def financial_info_main():
    while True:
        choice = input('Which one would you like to do?:\n\n1. Add an income to your history\n2. Add an expense to your history\n3. View your money history\n4. View money history within a certain number of weeks.\n5. Exit this part\n\n(1-5): ')

        if choice == '1':
            income()
        elif choice == '2':
            expense()
        elif choice == '3':
            display_csv()
        elif choice == '4':
            try:
                num_weeks = int(input('How many weeks would you like to check?: '))
                view_money_history(num_weeks)
            except ValueError:
                print("Enter a number next time.")
        elif choice == '5':
            print('\nGoing back to the main function.')
            break
        else:
            print('\nIncorrect option, try again.')