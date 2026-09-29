import csv
from pathlib import Path

DATA_FILE = Path("data/expenses.csv")


def save_expenses(expenses):
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(DATA_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["name", "category", "amount"]
        )
        writer.writeheader()
        writer.writerows(expenses)

    print("Expenses saved successfully!")


def load_expenses():
    if not DATA_FILE.exists():
        return []

    expenses = []

    try:
        with open(DATA_FILE, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row["name"] and row["category"] and row["amount"]:
                    expenses.append({
                        "name": row["name"],
                        "category": row["category"],
                        "amount": float(row["amount"])
                    })
    except (ValueError, KeyError):
        print("Warning: Could not read some saved expense data.")

    return expenses
