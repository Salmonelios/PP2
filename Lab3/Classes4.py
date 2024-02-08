class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def deposit(self, cash):
        print("Money has been added!")
        self.balance += cash
    def withdraw(self, cash):
        if cash <= self.balance:
            self.balance -= cash
            print("You were given", cash, f"the balance is {self.balance}")
        else:
            print("Orepation denied, your balance is low")

acc = Bank("Roman", 3000)
ac = Bank("Ali", 2500)
while 1:
    j = input()
    y = input()
    if y=="d":
        f = int(input())
        if j == "Roman":
            acc.deposit(f)
        elif j == "Ali":
            ac.deposit(f)
    elif y == "w":
        g = int(input())
        if j == "Roman":
            acc.withdraw(g)
        elif j == "Ali":
            ac.withdraw(g)
    elif j == "q":
        break
        