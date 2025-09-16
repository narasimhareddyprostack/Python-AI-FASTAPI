#read emp.json file and print emp names
import json 
fp=open('emp.json','r')
employees=json.load(fp)

for emp in employees:
    print(emp['ename'])