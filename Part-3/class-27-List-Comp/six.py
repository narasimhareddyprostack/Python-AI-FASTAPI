numbers=[1,2,3,4]
#create new list - for every element of list 
#by adding plus 1

#using for loop

new_numbers1=[]
for num in numbers:
    new_numbers1.append(num+1)
print(new_numbers1)

#using map with lambda
print(list(map(lambda n:n+1,numbers)))
#using map with functoin
def addplus(num):
    return num+1

print(list(map(addplus,numbers)))

new_numbers2=[num+1 for num in numbers]
print(new_numbers2)