import csv

def display_csv():
    try:
        # Open the CSV file in read mode
        with open('money_tracking.csv', 'r', newline='') as csvfile:
            file = list(csv.reader(csvfile))  # Read all rows into a list
            
            # Check if the file has only one row and that it only has the money value in the first column
            if len(file) == 1 and len(file[0]) == 1:
                print(f'Money: {file[0][0]}')  # Display the money value
            else:
                print("File contents:")
                for row in file:
                    print(", ".join(row))  # Join elements of the row and print them without brackets

    except FileNotFoundError:
        print("The file doesn't exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
display_csv()
