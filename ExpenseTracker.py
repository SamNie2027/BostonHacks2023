# from User import Users
# from ExpenseTracker import ExpenseTracker
from util import ExpenseTracker, User
import json

# class ExpenseTracker:
    
#     def __init__(self):
#         """ constructs 
#         """
#         self.balance = 0
#         self.expenses = []
    
#     def add_income(self, income):
#         self.balance += income
#         print(f"Income of ${income} added. Current balance: ${self.balance}")
    
#     def add_expense(self, amount, description):
#         if amount <= self.balance:
#             self.balance -= amount
#             self.expenses.append({"amount": amount, "description": description})
#             print(f"Expense of ${amount} for '{description}' added. Current balance: ${self.balance}")
#         else:
#             print("Insufficient funds. Expense not added.")

#     def display_summary(self):
#         print("\nExpense Tracker Summary:")
#         print(f"Current Balance: ${self.balance}")
#         print("\nExpenses:")
#         for expense in self.expenses:
#             print(f"- ${expense['amount']} for '{expense['description']}'")
    
#     def expense_distribution(self):
#         total = sum(float(expense['amount']) for expense in self.expenses)
#         result = []
#         for expense in self.expenses:
#             amount = float(expense['amount'])
#             description = expense['description']
#             percentage = (amount / total) * 100
#             result.append((description, percentage))
        
#         print("\nExpense Distribution:")
#         for description, percentage in result:
#             print(f"- '{description}': {percentage:.2f}%")
        
# def create(obj, username, password):
#     obj.username = username
#     obj.expense_tracker = 1)
#     obj.password = password    

def create(username, password):
    user = User(username, password)
    expense_tracker = ExpenseTracker(username)
    return user, expense_tracker

#def save_to_file(user, tracker, filename):
    user_data = {
        'username': user.username,
        'password': user.password,
        'expense_tracker': tracker.get_data()  # Assuming ExpenseTracker has a method to get its data
    }

    with open(filename, 'w') as file:
        json.dump(user_data, file)



def main():

    print("Welcome!")
    # user = User()

    while True:
        user_choice = input("Do you want to (1) Sign Up or (2) Log In: ")
        # print(user_choice == "1")
        if user_choice == "1":
            # def sign_up():
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            # new_user = create(username, password)
            new_user, tracker = create(username, password)
            new_user.save_to_file('user_data.json')
            print("Sign Up Successful!")


            # Create a new user and save to a file
            # new_user = User(username, password)
      
            # tracker = ExpenseTracker()
            # print(1
            # .username)
            # new_user.save_to_file(new_user, tracker, 'user_data.json') #The method in User.py and util.py take two arguments but this is passing in 3

            break

        elif user_choice == "2":
            # Log In
            entered_username = input("Enter your username: ")
            entered_password = input("Enter your password: ")

            # Load user data from file and attempt login
            try:
                existing_user = User.load_from_file('user_data.json')
                user = User(entered_username, entered_password)
                if user.login(entered_username, entered_password):
                    # Perform actions after successful login if needed
                    user.display_summary()
                    # user.display_average_income()
                    break
            except FileNotFoundError:
                print("No user data found. Please sign up first.")
                break

        else:
            print("Invalid choice. Please enter 1 or 2.")
    
    
    


    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Display Summary")
        print("4. Quit")
    
        choice = int(input("\nEnter choice: "))
        
        if choice == 1:
            tracker = ExpenseTracker(entered_username)
            user
            income = float(input("Enter income: "))
            tracker.add_income(income)
        elif choice == 2:
            amount = float(input("Enter the expense amount: "))
            description = input("Enter the expense description: ")
            tracker.add_expense(amount, description)
            print(tracker.expenses)
        elif choice == 3:
            tracker.display_summary()
            tracker.expense_distribution()
            print("-" * 30)
        elif choice == 4:
            print("Exiting Expense Tracker.")
            tracker.save_to_the_file("./user_data.json")
            break
        else:
            print("Invalid Choice.")
main()