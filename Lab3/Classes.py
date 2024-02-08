class String:
    def __init__(self):
        self.s = ""
    def getString(self):
        self.s = input()
    def printString(self):
        print(f"{self.s}".upper())

k = String()
k.getString()
k.printString()

