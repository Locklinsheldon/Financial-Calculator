from income import income
from expense import expense
from display_info import display_csv

def financial_info_main():
    while True:
        choice = input('Which one would you like to do?:\n\n1. Add an income to your history\n2. Add an expense to your history\n3. View your money history\n4. Exit this part\n\n(1-4): ')

        if choice == '1':
            income()
        elif choice == '2':
            expense()
        elif choice == '3':
            display_csv()
        elif choice == '4':
            print('\nGoing back to the main function.')
            break
        else:
            print('\nIncorrect option, try again.')

if __name__ == '__financial_info_main__':
    financial_info_main()