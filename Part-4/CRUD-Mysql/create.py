import mysql.connector
dbcon=mysql.connector.connect(host="localhost",
                              user='root',
                              password='root',
                              database='onedb')
print(dbcon)
cursor=dbcon.cursor()
print(type(cursor))
sql_st='''
        create table employees(
        eid int,
        ename varchar(32),
        esal float
        );
       '''
cursor.execute(sql_st)
dbcon.commit()
print("Table Created sucessfully!")
cursor.close()
dbcon.close()