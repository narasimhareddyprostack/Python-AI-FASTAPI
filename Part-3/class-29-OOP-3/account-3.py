class Account:
    def __init__(self,id,name,amount):
        self.acc__id=id
        self.acc_name=name 
        self.acc_bal=amount 
    def open_acc(self):
        print('Account Opened Successfully')
    def deposit(self,amount):
        self.acc_bal=self.acc_bal+amount

a1=Account(101,'Rahul',5000)
a1.deposit(500)
a1.deposit(1500)
print(a1.__dict__)

a2=Account(102,'Sonia',15000)
a2.deposit(150)
print(a2.__dict__)
a3=Account(103,'Priyanka',25000)
print(a3.__dict__)
