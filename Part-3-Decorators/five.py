def smart_div(func):
    def inner(a,b):
        if b==0:
            print("Buddy! cant divide by zero")
        else:
            return func(a,b)
    return inner

@smart_div
def division(a,b):
    print(a/b)

division(10,5)
division(10,1)
division(10,0)
division(10,2)