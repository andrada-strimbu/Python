# Design a bank account system with a base class Account and
# subclasses SavingsAccount and CheckingAccount.
# Implement methods for deposit, withdrawal, and interest calculation.

class Account:
    def __init__(self, accountNumber, balance=0):
        self.accountNumber = accountNumber
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"New balance: {self.balance} RON")

    def withdrawal(self, amount):
        if self.balance < amount:
            print("Solduri insuficiente!")
        else:
            self.balance -= amount
            print(f"New balance: {self.balance} RON")

    def interestCalculation(self):
        pass


class SavingsAccount(Account):
    def __init__(self, account_number, balance=0, interest_rate=0.02):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def interestCalculation(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print(f"Dobanda adaugata de:{interest}")


class CheckingAccount(Account):
    def __init__(self, account_number, balance=0, overdraft_limit=100):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdrawal(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"New balance: {self.balance} RON")
        else:
            print("Solduri insuficiente!")

    def interestCalculation(self):
        amount = self.balance + self.overdraft_limit;
        print(f"Fonduri alocate: {amount} RON")


def main():
    savings_account = SavingsAccount(account_number="SA123", balance=1000)
    checking_account = CheckingAccount(account_number="CA456", balance=500, overdraft_limit=200)

    savings_account.deposit(200)
    savings_account.interestCalculation()

    checking_account.withdrawal(300)
    checking_account.interestCalculation()
    checking_account.withdrawal(800)


main()
