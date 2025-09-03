#create dict object
emp={
    'eid':101,
    'ename':'Rahul',
    'esal':45000.45,
    'email':'rg@ibm.com',
}

#delete employee salary 
del emp['esal']
print(emp)

#delete dict/emp dict object

del emp 

print(emp)  #NameError