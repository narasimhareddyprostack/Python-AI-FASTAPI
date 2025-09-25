class Test:
    a=10
    def __init__(self):
        self.b=20
        self.c=30

    def m1(self):
        self.d=40 
    def m2(self):
        self.e=50
t1=Test()
t1.m1()
print(t1.__dict__)

t2=Test()
t2.m2()
print(t2.__dict__)
print(Test.__dict__)