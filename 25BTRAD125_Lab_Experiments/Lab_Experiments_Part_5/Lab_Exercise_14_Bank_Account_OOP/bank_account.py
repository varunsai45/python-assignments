print("========== BANK ACCOUNT SYSTEM ==========")


class BankAccount:
    next_account_number = 1001

    def __init__(self, holder_name, initial_balance=0.0):
        if not holder_name.strip():
            raise ValueError("Account holder name cannot be empty.")
        if initial_balance < 0:
            raise ValueError("Opening balance cannot be negative.")

        self.holder_name = holder_name.strip().title()
        self.account_number = f"SB{BankAccount.next_account_number}"
        BankAccount.next_account_number += 1
        self.__balance = 0.0
        self.transactions = []

        if initial_balance > 0:
            self.deposit(initial_balance, "Opening balance")

    def deposit(self, amount, note="Deposit"):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")

        self.__balance += amount
        self.transactions.append((note, amount, self.__balance))

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")

        if amount > self.__balance:
            raise ValueError(
                f"Insufficient balance. Available balance: Rs.{self.__balance:.2f}"
            )

        self.__balance -= amount
        self.transactions.append(("Withdrawal", -amount, self.__balance))

    def get_balance(self):
        return self.__balance

    def show_details(self):
        print("-" * 50)
        print(f"  Account Number : {self.account_number}")
        print(f"  Holder Name    : {self.holder_name}")
        print(f"  Balance        : Rs.{self.__balance:.2f}")
        print("-" * 50)

    def show_history(self):
        if not self.transactions:
            print("No transactions recorded for this account.")
            return

        print(f"\nTransaction history for {self.account_number} ({self.holder_name})")
        print("-" * 60)
        print(f"{'Type':<20} {'Amount':>12} {'Balance':>14}")
        print("-" * 60)
        for note, amount, balance in self.transactions:
            print(f"{note:<20} {amount:>12.2f} {balance:>14.2f}")
        print("-" * 60)


def read_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))
        except ValueError:
            print("Invalid amount! Enter a number.")
            continue

        if amount <= 0:
            print("Amount must be greater than zero.")
            continue

        return amount


def read_opening_balance():
    while True:
        try:
            amount = float(input("Enter opening balance (0 or more): "))
        except ValueError:
            print("Invalid amount! Enter a number.")
            continue

        if amount < 0:
            print("Opening balance cannot be negative.")
            continue

        return amount


def choose_account(accounts):
    if not accounts:
        print("No accounts available. Create an account first.")
        return None

    account_number = input("Enter account number: ").strip().upper()
    account = accounts.get(account_number)
    if account is None:
        print("Account not found.")
    return account


accounts = {}


def create_account():
    name = input("Enter account holder name: ").strip()
    if not name:
        print("Account holder name cannot be empty!")
        return

    try:
        opening_balance = read_opening_balance()
        account = BankAccount(name, opening_balance)
    except ValueError as error:
        print("Could not create account:", error)
        return

    accounts[account.account_number] = account
    print(f"Account created successfully. Account number: {account.account_number}")


def deposit_money():
    account = choose_account(accounts)
    if account is None:
        return

    amount = read_amount("Enter amount to deposit: ")
    try:
        account.deposit(amount)
    except ValueError as error:
        print("Transaction failed:", error)
        return

    print(f"Rs.{amount:.2f} deposited successfully.")
    print(f"Updated balance: Rs.{account.get_balance():.2f}")


def withdraw_money():
    account = choose_account(accounts)
    if account is None:
        return

    amount = read_amount("Enter amount to withdraw: ")
    try:
        account.withdraw(amount)
    except ValueError as error:
        print("Transaction failed:", error)
        return

    print(f"Rs.{amount:.2f} withdrawn successfully.")
    print(f"Updated balance: Rs.{account.get_balance():.2f}")


def balance_enquiry():
    account = choose_account(accounts)
    if account is None:
        return

    account.show_details()


def transaction_history():
    account = choose_account(accounts)
    if account is None:
        return

    account.show_history()


def display_all_accounts():
    if not accounts:
        print("No accounts available.")
        return

    print("\n" + "=" * 60)
    print("ALL BANK ACCOUNTS")
    print("=" * 60)
    print(f"{'Account No.':<15} {'Holder Name':<25} {'Balance':>15}")
    print("-" * 60)
    for account_number in sorted(accounts):
        account = accounts[account_number]
        print(
            f"{account.account_number:<15} {account.holder_name:<25} "
            f"{account.get_balance():>15.2f}"
        )
    print("=" * 60)


while True:
    print("\n1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Balance Enquiry")
    print("5. Transaction History")
    print("6. Display All Accounts")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ").strip()

    if choice == "1":
        create_account()
    elif choice == "2":
        deposit_money()
    elif choice == "3":
        withdraw_money()
    elif choice == "4":
        balance_enquiry()
    elif choice == "5":
        transaction_history()
    elif choice == "6":
        display_all_accounts()
    elif choice == "7":
        print("Exiting Bank Account System. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 7.")
