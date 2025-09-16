#read emp.json file and print  avail emp names
import json 
fp=open('emp.json','r')
employees=json.load(fp)

for emp in employees:
    if emp['avail'] ==True:
        print(emp['ename'])