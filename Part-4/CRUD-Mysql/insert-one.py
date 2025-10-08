import mysql.connector
dbcon=mysql.connector.connect(host="localhost",
                              user='root',
                              password='root',
                              database='onedb')
cursor=dbcon.cursor()
sql_st='''
        insert into employees
        values
        (101,'Rahul',45000.45);
       '''
cursor.execute(sql_st)
dbcon.commit()
print("Data Inserted sucessfully!")
cursor.close()
dbcon.close()