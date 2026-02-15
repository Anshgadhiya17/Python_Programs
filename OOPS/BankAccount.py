class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Balance:", self.balance)

name = input("Enter account holder name: ")
balance = float(input("Enter initial balance: "))

acc = BankAccount(name, balance)

choice = input("Deposit or Withdraw (d/w): ")
amount = float(input("Enter amount: "))

if choice == "d":
    acc.deposit(amount)
else:
    acc.withdraw(amount)

acc.show_balance()
