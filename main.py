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
    choice = input('Which one would you like to do?:\n\n1. ')