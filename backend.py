import json
import re  

# Database simulation 
users = []
expenses = []

def is_valid_email(email):
    return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email) is not None

def is_valid_mobile(mobile):
    return re.match(r"^\d{10}$", mobile) is not None

def add_user(email, name, mobile):

    try :
        
        user = {
            "email": email,
            "name": name,
            "mobile": mobile
        }
        users.append(user)
        print(f"User {name} added successfully.")
    except Exception as e:
        print(f"Error adding user: {str(e)}")

def add_expense(total_amount, participants, method, splits):
    try:
        expense = {
            "total_amount": total_amount,
            "participants": [p.strip() for p in participants],  
            "method": method,
            "splits": splits
        }
        expenses.append(expense)
        print("Expense added successfully.")
    except Exception as e:
        print(f"Error adding expense: {str(e)}")


def calculate_expenses():
    
    try:
        
        balance_sheet = {}
        for expense in expenses:
            for participant in expense['participants']:
                participant = participant.strip()  
                if participant not in balance_sheet:
                    balance_sheet[participant] = 0
                if expense['method'] == 'equal':
                    share = expense['total_amount'] / len(expense['participants'])
                    balance_sheet[participant] += share
                elif expense['method'] == 'exact':
                    if participant in expense['splits']:
                        balance_sheet[participant] += expense['splits'][participant]
                elif expense['method'] == 'percentage':
                    if participant in expense['splits']:
                        share = (expense['total_amount'] * expense['splits'][participant]) / 100
                        balance_sheet[participant] += share
        return balance_sheet
    except Exception as e:
        print(f"Error while calculating : {e}")
        
def download_balance_sheet(balance_sheet):

    try:
        
        balance_sheet_with_comments = {
            "_comment": "This balance sheet reflects the amounts owed by each user after all expenses are calculated.",
            "balances": balance_sheet  
        }

        with open("balance_sheet.json", "w") as f:
            json.dump(balance_sheet_with_comments, f, indent=4)
        print("Balance sheet downloaded as 'balance_sheet.json'.")
    except Exception as e:
        print(f"Error while downloading balance sheet: {e}")



#driver function
def main():
    while True:
        print("\n--- Daily Expenses Sharing Application ---")
        print("1. Add User")
        print("2. Add Expense")
        print("3. View Balance Sheet")
        print("4. Download Balance Sheet")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            email = input("Enter user email: ")
            # Validate email format
            if not is_valid_email(email):
                print("Error: Invalid email format.")
                continue
            
            name = input("Enter user name: ")
            mobile = input("Enter user mobile number (10 digits): ")
            # Validate mobile number
            if not is_valid_mobile(mobile):
                print("Error: Enter valid Mobile Number.")
                continue
            
            add_user(email, name, mobile)

        elif choice == '2':
            total_amount = float(input("Enter total expense amount: "))
            participants = input("Enter participants (comma-separated): ").split(",")
            method = input("Enter split method (equal, exact, percentage): ").lower()
            splits = {}
            if method == 'exact':
                for participant in participants:
                    splits[participant.strip()] = float(input(f"Enter exact amount for {participant.strip()}: "))
            elif method == 'percentage':
                for participant in participants:
                    splits[participant.strip()] = float(input(f"Enter percentage for {participant.strip()}: "))
                # Validate if percentages add up to 100
                if sum(splits.values()) != 100:
                    print("Error: Percentages do not add up to 100.")
                    continue
            
            add_expense(total_amount, participants, method, splits)

        elif choice == '3':
            balance_sheet = calculate_expenses()
            print("\n--- Balance Sheet ---")
            for user, amount in balance_sheet.items():
                print(f"{user}: {amount:.2f}")

        elif choice == '4':
            balance_sheet = calculate_expenses()
            download_balance_sheet(balance_sheet)

        elif choice == '5':
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


