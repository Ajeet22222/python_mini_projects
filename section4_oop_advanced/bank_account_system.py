import re


class Account:
    def __init__(self, account_number, holder_name, balance=0):
        self.__balance = balance
        self.account_number = account_number
        self.holder_name = holder_name

    def validate_account_number(self):
        pattern = r'^\d{10}$'
        return re.match(pattern, self.account_number) is not None

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return
        self.__balance += amount
        print(f"Rs.{amount:.2f} deposited successfully.")

    def get_balance(self):
        return self.__balance

    def display(self):
        print(f"  Account Number : {self.account_number}")
        print(f"  Holder Name    : {self.holder_name}")
        print(f"  Balance        : Rs.{self.__balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return
        if amount > self.__balance:
            print("Insufficient balance.")
            return
        self.__balance -= amount
        print(f"Rs.{amount:.2f} withdrawn successfully.")


class SavingsAccount(Account):
    def __init__(self, account_number, holder_name, balance=0):
        super().__init__(account_number, holder_name, balance)
        self.account_type = "Savings"
        self.minimum_balance = 1000

    def withdraw(self, amount):
        if self.get_balance() - amount < self.minimum_balance:
            print(f"Cannot withdraw. Minimum balance of Rs.{self.minimum_balance} must be maintained.")
            return
        super().withdraw(amount)


class CurrentAccount(Account):
    def __init__(self, account_number, holder_name, balance=0):
        super().__init__(account_number, holder_name, balance)
        self.account_type = "Current"
        self.overdraft_limit = 5000

    def withdraw(self, amount):
        if amount > self.get_balance() + self.overdraft_limit:
            print(f"Cannot withdraw. Exceeds overdraft limit of Rs.{self.overdraft_limit}.")
            return
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return
        print(f"Rs.{amount:.2f} withdrawn successfully.")


def create_account():
    print("\n1. Savings Account")
    print("2. Current Account")
    account_type = input("Select account type (1-2): ").strip()

    account_number = input("Enter 10 digit account number: ").strip()
    holder_name = input("Enter account holder name: ").strip()
    initial_balance = float(input("Enter initial balance: Rs."))

    if account_type == "1":
        account = SavingsAccount(account_number, holder_name, initial_balance)
    elif account_type == "2":
        account = CurrentAccount(account_number, holder_name, initial_balance)
    else:
        print("Invalid account type.")
        return None

    if not account.validate_account_number():
        print("Invalid account number. It must be exactly 10 digits.")
        return None

    print(f"{account.account_type} account created successfully.")
    return account


def main():
    print("=" * 40)
    print("       Bank Account System")
    print("=" * 40)

    account = None

    while True:
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        print("-" * 40)

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            account = create_account()

        elif choice == "2":
            if account is None:
                print("Please create an account first.")
            else:
                amount = float(input("Enter amount to deposit: Rs."))
                account.deposit(amount)

        elif choice == "3":
            if account is None:
                print("Please create an account first.")
            else:
                amount = float(input("Enter amount to withdraw: Rs."))
                account.withdraw(amount)

        elif choice == "4":
            if account is None:
                print("Please create an account first.")
            else:
                account.display()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


main()