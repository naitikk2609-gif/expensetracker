def get_valid_amount():
    while True:
        value = input("Enter amount: ").strip()

        try:
            amount = float(value)

            if amount <= 0:
                print("Amount must be greater than 0.")
            else:
                return amount

        except ValueError:
            print("Please enter a valid number.")
