# Main function

from accounts import view_asset
from accounts import create_new_account
from financial_info_main import financial_info_main
from goals import goal_managment
from limits import limit_managment
from pie_charts import 


def main():
    print('This is a financial Calculator which can do a ton of things.\n')
    while True:
        choice = input('Which one would you like to do?:\n\n1. Accounts\n2. Financial Information (Income and Expenses)\n3. Goals\n4. Money Limits\n5. View Pie Charts of Your Data\n6. Exit the program.\n\n(1-6): ')

        if choice == '1':
            while True:
                account_choice = input("Which one would you like to do?:\n\n1. View an account's information\n2. Create a new account\n3. Go back\n\n(1 or 2): ")
                if account_choice == '1':
                    view_asset()
                elif account_choice == '2':
                    create_new_account()
                elif account_choice == '3':
                    break
                else:
                    print('Incorrect option, try again.')
        elif choice == '2':
            financial_info_main()
        elif choice == '3':
            goal_managment()
        elif choice == '4':
            limit_managment()
        