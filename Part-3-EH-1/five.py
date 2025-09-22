try:
    a=int(input("Enter First Number:"))
    b=int(input('Enter Second Number:'))
    print(a/b)
    
except (TypeError,ValueError,ZeroDivisionError) as err:
    print(err)

print("GM")