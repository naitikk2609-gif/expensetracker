import unittest
from expense_manager import ExpenseManager
from analysis import calculate_total, category_totals, find_highest_expense


class TestExpenseTracker(unittest.TestCase):

    def setUp(self):
        self.manager = ExpenseManager()
        self.manager.add_expense("Lunch", "Food", 120)
        self.manager.add_expense("Bus", "Travel", 40)
        self.manager.add_expense("Snacks", "Food", 60)

    def test_number_of_expenses(self):
        self.assertEqual(len(self.manager.get_expenses()), 3)

    def test_total_expense(self):
        self.assertEqual(calculate_total(self.manager.expenses), 220)

    def test_category_totals(self):
        totals = category_totals(self.manager.expenses)
        self.assertEqual(totals["Food"], 180)
        self.assertEqual(totals["Travel"], 40)

    def test_highest_expense(self):
        highest = find_highest_expense(self.manager.expenses)
        self.assertEqual(highest["name"], "Lunch")
        self.assertEqual(highest["amount"], 120)


if __name__ == "__main__":
    unittest.main()
