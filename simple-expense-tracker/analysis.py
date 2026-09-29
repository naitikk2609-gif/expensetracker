def calculate_total(expenses):
    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    return total


def show_total(expenses):
    if len(expenses) == 0:
        print("No expenses found.")
        return

    total = calculate_total(expenses)
    print(f"Total Expense: ₹{total:.2f}")


def category_totals(expenses):
    categories = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in categories:
            categories[category] = categories[category] + amount
        else:
            categories[category] = amount

    return categories


def show_category_summary(expenses):
    if len(expenses) == 0:
        print("No expenses found.")
        return

    categories = category_totals(expenses)

    print("\n--- Category Summary ---")
    for category in categories:
        print(f"{category}: ₹{categories[category]:.2f}")


def find_highest_expense(expenses):
    if len(expenses) == 0:
        return None

    highest = expenses[0]

    for expense in expenses:
        if expense["amount"] > highest["amount"]:
            highest = expense

    return highest


def show_highest_expense(expenses):
    highest = find_highest_expense(expenses)

    if highest is None:
        print("No expenses found.")
        return

    print("\n--- Highest Expense ---")
    print("Name:", highest["name"])
    print("Category:", highest["category"])
    print(f"Amount: ₹{highest['amount']:.2f}")
