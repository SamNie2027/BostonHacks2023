import User

class ExpenseTracker:
    
    def __init__(self):
        """ constructs 
        """
        self.balance = 0
        self.expenses = []
    
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
        
    
def main():
        
    tracker = ExpenseTracker()
    
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Display Summary")
        print("4. Quit")
    
        choice = int(input("\nEnter choice: "))
        
        if choice == 1:
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
            break
        else:
            print("Invalid Choice.")
main()