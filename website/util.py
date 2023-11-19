import json

class ExpenseTracker:
    def __init__(self, username):
        """ constructs 
        """
        self.balance = 0
        self.expenses = []
        self.username = username
    def save_to_the_file(self, filename):
        user_data = {
            'username': self.username,
            'expenses': self.expenses,
            'balance': self.balance
        }

        with open(filename, 'w') as file:
            json.dump(user_data, file)
        print(f"Expense data and summary for user {self.username} saved to {filename}")



    def add_income(self, income):
        self.balance += income
        print(f"Income of ${income} added. Current balance: ${self.balance}")
    
    def add_expense(self, amount, description):
        if amount <= self.balance:
            self.balance -= amount
            self.expenses.append({"amount": amount, "description": description})
            print(f"Expense of ${amount} for '{description}' added. Current balance: ${self.balance}")
        else:
            print("Insufficient funds. Expense not added.")

    def display_summary(self):
        print("\nExpense Tracker Summary:")
        print(f"Current Balance: ${self.balance}")
        print("\nExpenses:")
        for expense in self.expenses:
            print(f"- ${expense['amount']} for '{expense['description']}'")
    
    def expense_distribution(self):
        total = sum(float(expense['amount']) for expense in self.expenses)
        result = []
        for expense in self.expenses:
            amount = float(expense['amount'])
            description = expense['description']
            percentage = (amount / total) * 100
            result.append((description, percentage))
        
        print("\nExpense Distribution:")
        for description, percentage in result:
            print(f"- '{description}': {percentage:.2f}%")

    def get_data(self):
        data = {
            'username': self.username,
            'expenses': [{'name': exp.name, 'amount': exp.amount} for exp in self.expenses]
        }
        return data

class User:
    def __init__(self, username, password):
        self.username = username
        self.expense_tracker = ExpenseTracker(username)
        self.password = password

    # def create(self, username, password):
        # self.username = username
        # self.expense_tracker = ExpenseTracker()
        # self.password = password



    # def add_income(self, income):
    #     self.expense_tracker.add_income(income)

    # def add_expense(self, amount, description):
    #     self.expense_tracker.add_expense(amount, description)

    def display_summary(self):
        print(f"\nSummary for User {self.username}:")
        self.expense_tracker.display_summary()

    def display_average_income(self):
        avg_income = self.expense_tracker.average_income()
        print(f"Average Income for User {self.username}: ${avg_income}")
    
    def __eq__(self, other):
        if self.username == other.username and self.password == other.password:
            return True
        else:
            return False

    def login(self, entered_username, entered_password):
        other = User(entered_username, entered_password)
        if self == other:
            print("Login Successful!")
            return True
        else:
            print("Your Username or Password is Incorrect. Try Again.")
            return False

    def save_to_file(self, filename):
        user_data = {
            'username': self.username,
            'password': self.password,
            'expense_tracker': self.expense_tracker.get_data()  # Assuming ExpenseTracker has a method to get its data
        }

        with open(filename, 'w') as file:
            json.dump(user_data, file)

    # @classmethod
    def load_from_file(filename):
        with open(filename, 'r') as file:
            user_data = json.load(file)

        loaded_user = user_data['username'], user_data['password'], user_data['expense_tracker']
        # print(loaded_user)
        # loaded_user.expense_tracker.load_data(user_data['expense_tracker'])
        return loaded_user