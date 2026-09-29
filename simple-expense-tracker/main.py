from expense_manager import ExpenseManager
from analysis import show_total, show_category_summary, show_highest_expense
from storage import save_expenses, load_expenses
from validation import get_valid_amount


def add_expense(manager):
    print("\n--- Add Expense ---")
    name = input("Enter expense name: ").strip()
    category = input("Enter category: ").strip()

    if name == "" or category == "":
        print("Name and category cannot be empty.")
        return

    amount = get_valid_amount()
    manager.add_expense(name, category, amount)
    print("Expense added successfully!")


def view_expenses(manager):
    print("\n--- All Expenses ---")

    if len(manager.expenses) == 0:
        print("No expenses found.")
        return

    for number, expense in enumerate(manager.expenses, start=1):
        print(f"{number}. {expense['name']} | "
              f"{expense['category']} | ₹{expense['amount']:.2f}")


def main():
    manager = ExpenseManager()
    manager.expenses = load_expenses()

    while True:
        print("\n==============================")
        print("     SIMPLE EXPENSE TRACKER")
        print("==============================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Category Summary")
        print("5. Highest Expense")
        print("6. Save Expenses")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense(manager)
        elif choice == "2":
            view_expenses(manager)
        elif choice == "3":
            show_total(manager.expenses)
        elif choice == "4":
            show_category_summary(manager.expenses)
        elif choice == "5":
            show_highest_expense(manager.expenses)
        elif choice == "6":
            save_expenses(manager.expenses)
        elif choice == "7":
            save_expenses(manager.expenses)
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()
