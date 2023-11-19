import json
# from User import User
# from ExpenseTracker import ExpenseTracker


# additional_functions.py

from util import ExpenseTracker, User

# x = User()
def create(obj, username, password):
    obj.username = username
    obj.expense_tracker = ExpenseTracker()
    obj.password = password



    # def add_income(self, income):
    #     self.expense_tracker.add_income(income)

    # def add_expense(self, amount, description):
    #     self.expense_tracker.add_expense(amount, description)

    # def display_summary(self):
    #     print(f"\nSummary for User {self.username}:")
    #     self.expense_tracker.display_summary()

    # def display_average_income(self):
    #     avg_income = self.expense_tracker.average_income()
    #     print(f"Average Income for User {self.username}: ${avg_income}")
    
    # def __eq__(self, other):
    #     if self.username == other.username and self.password == other.password:
    #         return True
    #     else:
    #         return False

    # def login(self, entered_username, entered_password):
    #     other = User(entered_username, entered_password)
    #     if self == other:
    #         print("Login Successful!")
    #         return True
    #     else:
    #         print("Your Username or Password is Incorrect. Try Again.")
    #         return False

    # def save_to_file(self, filename):
    #     user_data = {
    #         'username': self.username,
    #         'password': self.password,
    #         'expense_tracker': self.expense_tracker.get_data()  # Assuming ExpenseTracker has a method to get its data
    #     }

    #     with open(filename, 'w') as file:
    #         json.dump(user_data, file)

    # @classmethod
    # def load_from_file(cls, filename):
    #     with open(filename, 'r') as file:
    #         user_data = json.load(file)

    #     loaded_user = cls(user_data['username'], user_data['password'])
    #     loaded_user.expense_tracker.load_data(user_data['expense_tracker'])
    #     return loaded_user