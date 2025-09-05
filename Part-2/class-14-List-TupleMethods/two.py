numbers=[10,20,30,10,8]
#index   0   1  2  3  4
#create - methods
#Read - Methods
print(numbers)
print(numbers.index(20))   # 1
#print(numbers.index(200))  #ValueError-200 is not in list
print(numbers.count(10))   # 2 Times
#update - Methods
numbers.append(25)
print('After Appending element')
print(numbers)
numbers.insert(1,2)
print(numbers)
numbers.sort()
numbers.reverse()
print(numbers)   #Natural Sorting Order


#delete - Methods