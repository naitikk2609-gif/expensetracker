class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, name, category, amount):
        expense = {
            "name": name,
            "category": category,
            "amount": amount
        }
        self.expenses.append(expense)

    def get_expenses(self):
        return self.expenses
