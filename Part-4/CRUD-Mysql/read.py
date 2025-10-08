import mysql.connector
from mysql.connector import 
dbcon=mysql.connector.connect(host="localhost",
                              user='root',
                              password='root',
                              database='onedb')
cursor=dbcon.cursor()
cursor.execute("Select *from employees")
employees=cursor.fetchall()
print(type(employees))
for emp in employees:
    print(emp) 

print("Done")
 