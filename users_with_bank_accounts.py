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

class User:		# here's what we have so far
    def __init__(self, name, email, accountNum):
        self.name = name
        self.email = email
        self.accountNum = accountNum
        self.account = BankAccount(int_rate=0.02, balance=0)
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account.deposit(amount)
        print(self.account.balance)
        return self
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        print(self.accountbalance)
        return self
    def display_user_balance(self):
        print("User", self.name,"account:", self.accountNum,"Balance:", self.account.balance)
        return self

# SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to

mei = User("Mei Manzo", "email@gmail.com", "account1")

mei.make_deposit(100).display_user_balance()

mei = User("Mei Manzo", "email@gmail.com", "account2")

mei.make_deposit(2000).display_user_balance()