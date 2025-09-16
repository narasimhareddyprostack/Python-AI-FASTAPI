#read emp.json file and print emp names
import json 
fp=open('emp.json','r')
employees=json.load(fp)
print(type(employees))
print(employees)