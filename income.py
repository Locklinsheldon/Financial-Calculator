import csv
from datetime import datetime

def income(): #The income function
    try:
        # Open the file in 'r+' mode (read and write)
        with open('money_tracking.csv', 'r+', newline='') as csvfile:
            # Read all rows into a list
            file = list(csv.reader(csvfile))
            
            # If the file is empty or the first row has '0', initialize with '0'
            if not file or file[0][0] == '0':
                file = [['0']]  # Initialize with '0' as the first row

            # Get the current money value from the first row
            money = int(file[0][0])  
            print(f"Current money value: ${money}")

            # Ask for new income and reason
            while True:
                try:
                    new_income = int(input('How much money did you get?: '))
                    reason = input(f'How did you get ${new_income} dollars?: ')

                    # Validate that the reason is not empty
                    if not reason:
                        print("Please provide a valid reason.")
                        continue
                    
                    # Add the new income to the existing money value
                    updated_money = money + new_income

                    # Update the first row with the new total money value
                    file[0] = [str(updated_money)]  # Replace the first row with the new total money

                    # Get the current date
                    now = datetime.now()
                    date = now.strftime("%Y-%m-%d")

                    # Append the new income entry (Date, Money, Reason)
                    new_entry = [f"Date: {date}, Money: {new_income}, Reason: {reason}"]
                    file.append(new_entry)  # Add the new entry to the list

                    # Now write everything back to the file (updated money and new entry)
                    with open('money_tracking.csv', 'w', newline='') as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerows(file)  # Write all rows back to the file

                    print("Data successfully updated!")
                    break  # Exit the loop once everything is written

                except ValueError:
                    print('Incorrect input, please enter a valid number for the income.')

            # Show updated file contents
            print("\nUpdated File Contents:")
            with open('money_tracking.csv', 'r') as csvfile:
                for row in file:
                    print(", ".join(row))  # Join elements of the row and print them without brackets

    except IOError:
        print("An error occurred while trying to read or write the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
income()
