import csv

def display_csv():
    try:
        # Open the CSV file in read mode
        with open('money_tracking.csv', 'r', newline='') as csvfile:
            file = csv.reader(csvfile)
            print(f'Money: {(", ".join(next(file)))}')
            list(file)

            if len(file) == 1:
                print('There is nothing in the file to print except for the money.')
            else:
                # Print each row in the CSV
                print("File contents:")
                for row in file:
                    print(", ".join(row))  # Join elements of the row and print them without brackets
    except FileNotFoundError:
        print("The file doesn't exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
display_csv()
