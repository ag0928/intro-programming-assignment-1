class Bank:
    def __init__(self, accno, balance):
        self.accno = accno
        self.balance = balance

    def deposit(self, amt):
        self.balance = self.balance + amt

    def withdraw(self, amt):
        self.balance = self.balance - amt

    def show(self):
        print(self.accno, self.balance)


bank1 = Bank("749522454", 488852)

bank1.show()
bank1.deposit(1000)
bank1.show()
bank1.withdraw(500)
bank1.show()