numbers=[1,2,3,4,5,6,7,8,9,10]
#collect all even numbers in list
def verify(num):
    return num%2 ==0

even_numbers=list(filter(verify,numbers))

print(numbers)
print(even_numbers)