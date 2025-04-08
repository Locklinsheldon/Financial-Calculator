# Main function

from accounts import view_asset
from accounts import create_new_account
from display_info import display_csv
from expense import expense
from financial_info_main import financial_info_main
from goals import goal_managment
from goals import set_goals
from goals import track_goals
from goals import advance_goals
from income import income
from limits import limit_managment
from limits import set_limits
from limits import compare_limits
from pie_charts import pie_charts

def main():
    print('This is a financial Calculator which can do a ton of things.\n')
    while True:
        choice = input('Which one would you like to do?:\n\n1. Accounts\n2. Financial Information (Income and Expenses)\n3. Goals\n4. Money Limits\n5. View Pie Charts of Your Data\n6. Exit the program.')