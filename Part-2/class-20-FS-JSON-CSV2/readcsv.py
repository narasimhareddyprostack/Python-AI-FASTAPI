import csv 
fp=open('emp.csv','r')
emp_reader=csv.reader(fp)
employees=list(emp_reader)
print(employees)

for emp in employees[1:]:
    print(emp[1])