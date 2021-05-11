class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance +=amount
        return self
    def withdraw(self, amount):
        self.balance -=amount
        return self
    def display_account_info(self):
        print("Balance:",self.balance)
        return self
    def yield_interest(self):
        if self.int_rate > 0:
            self.int_rate *= self.balance
            print("Calculated interest:",self.int_rate)
        return self
monty = BankAccount(.02, 200)
mei = BankAccount(.01, 200)

#To the first account, make 3 deposits and 1 withdrawal, then calculate interest and display the account's info all in one line of code (i.e. chaining)
monty.deposit(50).deposit(50).deposit(100).withdraw(100).yield_interest().display_account_info()

# To the second account, make 2 deposits and 4 withdrawals, then calculate interest and display the account's info all in one line of code (i.e. chaining)
mei.deposit(100).deposit(20).withdraw(10).withdraw(50).withdraw(10).withdraw(1).yield_interest().display_account_info()