class Account:

    def __init__(self,id,name,amount):
        self.acc_id=id 
        self.acc_name=name 
        self.acc_bal=amount 
        
    def open_account(self):
        print("Account Opened Successfully")

a1=Account(101,'RG',5000)
a2=Account(102,'SG',15000)
a3=Account(103,'PG',25000)

print(a1.__dict__)
print(a2.__dict__)
print(a3.__dict__)