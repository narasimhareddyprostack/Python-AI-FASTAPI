class Account:

    def open_acc(self):
        print("Account Opened Successfully!")

    def deposit(self):
        print("Amount Deposited Successfully!")

    def withdrawl(self):
        print("Insuffient Bal!")

    def get_bal(self):
        print("Servre Busy")

    def close_acc(self):
        print("Bal is -ve. pls deposit more")

a1= Account()
a2= Account()

a1.open_acc()
a1.deposit()
a1.withdrawl()
a1.get_bal()
a1.close_acc()