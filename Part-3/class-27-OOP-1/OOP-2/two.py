class Account:
    def open_account(self):
        print("Account opened Successfully!")

    def deposit_amount(self,amount):
        print(amount,":Amount Deposited")
        
    def get_Bal(self):
        return 0
a1=Account()
a1.open_account()
a1.deposit_amount(5000)
a1.deposit_amount(1500)