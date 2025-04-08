# Connor Pavicic, View a specific time period for money logs.

import csv
from datetime import datetime, timedelta

def view_money_history(weeks):
    #Calculate date cutoff
    today = datetime.today()
    cutoff_date = today - timedelta(weeks=weeks)

    #Read the csv
    with open("money_tracking.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        print(f"Entries in the last {weeks} week(s):\n")

        found = False

        for row in reader:
            if not row:
                continue
            entry = row[0] #Get the string
            try:
                # Extract string date
                date_str = entry.split(",")[0].replace("Date: ", "").strip()
                entry_date = datetime.strptime(date_str, "%Y-%m-%d")

                if entry_date >= cutoff_date:
                    print(entry)
                    found = True
            except Exception as e:
                print("Error with line {entry}")
                print(f"Error: {e}")
        
        if not found:
            print('No entries found within that time span.')