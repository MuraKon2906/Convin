# Convin - Daily Expenses Sharing Application

This application is designed to help users manage and share expenses among participants. It allows you to add users, track expenses, view a balance sheet, and download the balance sheet as a JSON file.

## Features

- **Add User**: Allows you to add a user with their email, name, and mobile number.
- **Add Expense**: Lets you input an expense, specifying the total amount, participants, the method of splitting the expense (equal, exact, percentage), and any necessary splits for the specific participants.
- **View Balance Sheet**: Displays the balance sheet showing how much each user owes or is owed after all expenses have been accounted for.
- **Download Balance Sheet**: Saves the current balance sheet as a JSON file for record-keeping.
- **Exit**: Terminates the application.

## Code Explanation

### Imports
```python
import json
import re  
```
- `json`: For handling JSON data (loading and saving the balance sheet).
- `re`: For regular expressions to validate email and mobile formats.

### Data Structures
- `users`: A list to store user information.
- `expenses`: A list to store expense records.

### Validation Functions
- **`is_valid_email(email)`**: Checks if the email format is valid using a regular expression.
- **`is_valid_mobile(mobile)`**: Validates the mobile number to ensure it consists of exactly 10 digits.

### Core Functions
- **`add_user(email, name, mobile)`**: Adds a new user to the `users` list.
- **`add_expense(total_amount, participants, method, splits)`**: Records an expense along with the participants and the method of splitting.
- **`calculate_expenses()`**: Calculates the total amounts owed by each user based on the recorded expenses.
- **`download_balance_sheet(balance_sheet)`**: Saves the balance sheet as a JSON file.

### Main Functionality
- **`main()`**: The driver function that presents a menu to the user, allowing them to choose an action.

## How to Use the Application

1. **Run the Application**: Execute the Python script in your terminal or command line. Ensure you have Python installed.
2. **Add Users**:
   - Choose option `1` to add a user.
   - Provide a valid email address, name, and a 10-digit mobile number.
3. **Add Expenses**:
   - Choose option `2` to add an expense.
   - Input the total expense amount and specify the participants.
   - Select a method to split the expenses: `equal`, `exact`, or `percentage`.
4. **View Balance Sheet**:
   - Choose option `3` to view the current balance sheet. It will display each user's balance based on the recorded expenses.
5. **Download Balance Sheet**:
   - Choose option `4` to download the balance sheet as `balance_sheet.json`. This file will contain all balances and a comment regarding its content.
6. **Exit**:
   - Choose option `5` to exit the application.

## Notes
- Ensure that all inputs are valid; otherwise, appropriate error messages will be displayed.
- The balance sheet will automatically update as new expenses are added.
