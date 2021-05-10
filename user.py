# For this assignment, we'll add some functionality to the User class:
# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
# display_user_balance(self) - have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150
# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance

class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance += amount	# the specific user's account increases by the amount of the value received
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print("User", self.name,"Balance:", self.account_balance)
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance +=amount

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
mei = User("Mei Manzo", "email@gmail.com")

# Have the first user make 3 deposits and 1 withdrawal and then display their balance:
guido.make_deposit(100)
guido.make_deposit(200)
guido.make_deposit(700)
guido.make_withdrawal(200)
print(guido.account_balance)	# output: 800

#Have the second user make 2 deposits and 2 withdrawals and then display their balance:
monty.make_deposit(100)
monty.make_deposit(500)
monty.make_withdrawal(500)
monty.make_withdrawal(5)
print(monty.account_balance)

#Have the third user make 1 deposits and 3 withdrawals and then display their balance:
mei.make_deposit(1000)
mei.make_withdrawal(50)
mei.make_withdrawal(500)
mei.make_withdrawal(300)
print(mei.account_balance)

#  BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances
mei.make_deposit(1000)
mei.transfer_money(guido, 300)
print("Mei's balance:", mei.account_balance)
print("Guido's balance:", guido.account_balance)

