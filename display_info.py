import csv

def display_csv():
    try:
        # Open the CSV file in read mode
        with open('money_tracking.csv', 'r', newline='') as csvfile:
            file = csv.reader(csvfile)  # Read the file as a CSV

            # Fetch the first row (money value)
            first_row = next(file, None)  # Get the first row, default to None if file is empty

            if first_row is None:  # Check if the file is empty
                print("The file is empty.")
                return

            money = ", ".join(first_row)  # Convert it to a string without brackets

            print(f'Money: {money}')  # Display the money value from the first row

            # Print the rest of the rows
            print("\nFile contents:")
            for row in file:
                print(", ".join(row))  # Join elements of the row and print them without brackets

    except FileNotFoundError:
        print("The file doesn't exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
display_csv()
