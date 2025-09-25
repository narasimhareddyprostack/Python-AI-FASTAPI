class Test:
    def __init__(self):
        print("constructor is special method")
    def m1(self):
        print("m1 method - instance method")
    @classmethod
    def m2(cls):
        print("m2 method - class method")
    @staticmethod
    def m3():
        print("m3 method - static method")
t1=Test()
t2=Test()
