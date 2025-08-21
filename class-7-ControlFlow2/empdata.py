employees=[
    {'eid':101,'ename':'Rahul','gender':'Male'},
    {'eid':102,'ename':'Sonia','gender':'Female'},
    {'eid':103,'ename':'Priyanka','gender':'Female'},
]
#print male/female employee names

for employee in employees:
    if employee['gender'] =='Female':
        print("Employee Name:", employee['ename'])
