#create
s1=set()   #empty set object
s2={10,20,10,20}
#read
print(s2)  #{20,10}  - duplicates are no allowed
#update
s2.add(30) #{10,20,30}
print(s2)  
s2.update({40,50,60})   #{50, 20, 40, 10, 60, 30}
print(s2)
#delete
