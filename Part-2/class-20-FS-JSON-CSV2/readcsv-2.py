import csv 
fp=open('emp.csv','r')
emp_data=csv.reader(fp)

for emp in list(emp_data)[1:]:
    print(emp)