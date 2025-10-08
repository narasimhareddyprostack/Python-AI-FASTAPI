import mysql.connector
dbcon=mysql.connector.connect(host="localhost",
                              user='root',
                              password='root',
                              database='onedb')
cursor=dbcon.cursor()
sql_st='''
        insert into employees(eid,ename,esal)
        values
        (%s,%s,%s);
       '''
employee_data=[
    (102,'Sonia',55000.55),
    (103,'Priya',65000.55),
    (104,'Modi',75000.55),
]
cursor.executemany(sql_st,employee_data)
dbcon.commit()
print("Data Inserted sucessfully!")
cursor.close()
dbcon.close()