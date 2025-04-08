#Pie charts done by Lizzy S
import csv
from accounts import create_new_account, view_asset
import matplotlib.pyplot as plt

def pie_charts():
    result = get_info()
    if not result:
        print("No data returned. Exiting pie chart function.")
        return

    expense = len(result)

    if expense == 9:
        label = 'Budgeting'
        categories = ['Savings', 'House', 'Utilities', 'Insurance', 'Food', 'Entertainment', 'Healthcare', 'Phone', 'Pet']
    elif expense == 6:
        label = 'Services'
        categories = ['Utilities', 'Insurance', 'Food', 'Entertainment', 'Healthcare', 'Phone']
    elif expense == 12 or expense == 11:
        label = 'All'
        categories = ['Checkings', 'Salary', 'Goal', 'Savings', 'House', 'Utilities', 'Insurance', 'Food', 'Entertainment', 'Healthcare', 'Phone']
        if expense == 12:
            categories.append('Pet')
    else:
        print("Unexpected error occurred, cannot create pie chart.")
        return

    # Create an "explode" list to separate large slices
    explode = [0.05 if value > sum(result) * 0.2 else 0 for value in result]

    # Hide tiny slices
    def autopct_format(pct):
        return f'{pct:.2f}%' if pct > 3 else ''

    # Plot the pie chart
    fig, ax = plt.subplots()
    ax.pie(
        result,
        labels=categories,
        autopct=autopct_format,
        explode=explode,
        startangle=90,
        wedgeprops={'edgecolor': 'black'}
    )
    ax.legend(categories, title="Categories", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    plt.title(f"Expense: {label}")
    plt.axis('equal')
    plt.tight_layout()
    plt.show()


def get_info():
    user = input('Enter your username:\n').strip()
    found = False
    user_row = None

    try:
        with open('financial_data.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            data = list(reader)

            for row in data:
                if row and row[0] == user:
                    password = input("Enter your password:\n").strip()
                    if row[1] == password:
                        print("Login successful!")
                        found = True
                        user_row = row
                        break
                    else:
                        print("Incorrect password.")
                        return None
    except FileNotFoundError:
        print("Error: 'finacial_data.csv' file not found.")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

    if not found:
        print("Account not found.")
        create_account = input("Create a new account?\n1) Yes\n2) No\n").strip()
        if create_account == '1':
            create_new_account(user)
            return get_info()
        else:
            print("Exiting...")
            return None

    ask = input('Would you like to get a pie chart of your data?\n1) Yes\n2) No\n').strip()
    if ask == '1':
        choice = input('What expense category?\n1) Budgeting\n2) Services\n3) ALL\n').strip()
        try:
            if choice == '1':
                return [float(i) for i in user_row[5:14]]  # Savings to Pet
            elif choice == '2':
                return [float(i) for i in user_row[7:13]]  # Utilities to Phone
            elif choice == '3':
                return [float(i) for i in user_row[2:14]]  # Checkings to Pet
            else:
                print('Invalid choice.')
                return None
        except (IndexError, ValueError) as e:
            print(f"Error reading financial data: {e}")
            return None
    elif ask == '2':
        option = input("Would you like to view a specific asset?\n1) Yes\n2) No\n").strip()
        if option == '1':
            view_asset(user_row)
        else:
            print("Exiting...")
        return None
    else:
        print('Invalid input.')
        return None


# Optional: run pie_charts automatically
if __name__ == "__main__":
    pie_charts()
