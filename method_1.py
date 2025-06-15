class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

acc = BankAccount("Gowtham")
acc.deposit(500)
print(acc.owner, acc.balance) 
