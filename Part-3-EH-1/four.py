try:
    a=int(input("Enter First Number:"))
    b=int(input('Enter Second Number:'))
    print(a/b)
    
except ValueError as ve:
    print(ve)
except ZeroDivisionError as err:
    print(err)

print("GM")