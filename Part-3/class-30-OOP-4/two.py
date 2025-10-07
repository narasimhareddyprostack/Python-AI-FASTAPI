class Order:
    ''' created by Narasimha '''
    def __init__(self,id,name,price):
        print("constructor is special method") 
        self.order_id=id 
        self.details=name 
        self.price=price
        
    def add_discount(self):
        self.discount=50
    @classmethod
    def check_avail(cls):
        cls.avail=True

o1=Order(11,'MP1',35)
o2=Order(12,'MP2',40)
o3=Order(13,'MP3',45)
o1.add_discount()
o2.add_discount()
o1.check_avail()

print(o1.__dict__)
print(o2.__dict__)
print(o3.__dict__)
print(Order.__dict__)  