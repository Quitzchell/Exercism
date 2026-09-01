class BankAccount:
    def __init__(self):
        self.account_open = False
        self.balance = 0

    def get_balance(self):
        if self.account_open:
            return self.balance
        else:
            raise ValueError("account not open")

    def open(self):
        if not self.account_open:
            self.account_open = True
        else:
            raise ValueError("account already open")

    def deposit(self, amount):
        if not self.account_open:
            raise ValueError("account not open")

        if amount < 0:
            raise ValueError("amount must be greater than 0")

        self.balance += amount

    def withdraw(self, amount):
        if not self.account_open:
            raise ValueError("account not open")

        if amount < 0:
            raise ValueError("amount must be greater than 0")

        if self.balance - amount < 0:
            raise ValueError("amount must be less than balance")

        self.balance -= amount



    def close(self):
        if self.account_open:
            self.account_open = False
            self.balance = 0
        else:
            raise ValueError("account not open")