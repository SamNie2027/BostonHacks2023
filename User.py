class User:
    def __init__(self, username, password):
        self.username = username
        self.expense_tracker = ExpenseTracker()
        self.password = password

    def add_income(self, income):
        self.expense_tracker.add_income(income)

    def add_expense(self, amount, description):
        self.expense_tracker.add_expense(amount, description)

    def display_summary(self):
        print(f"\nSummary for User {self.username}:")
        self.expense_tracker.display_summary()

    def display_average_income(self):
        avg_income = self.expense_tracker.average_income()
        print(f"Average Income for User {self.username}: ${avg_income}")
    def login(self, entered_password):
        return entered_password == self.password