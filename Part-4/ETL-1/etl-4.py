import requests,mysql.connector,json,csv 
#Extract Data 
response_data=requests.get('https://dummyjson.com/users')
users=response_data.json()['users']
#Transform 
new_users=[]
for user in users:
    new_users.append((user['id'],
                      user['username'],
                      user['email'],
                      user['gender']))
print(new_users)

#load 
dbcon=None 
try:
    dbcon=mysql.connector.connect(host='localhost', user='root',password='root',database='onedb')
    cursor=dbcon.cursor()
    sql_st='''
            insert into users()
            values
            (%s,%s,%s,%s)
            ''' 
    cursor.executemany(sql_st,new_users)
    dbcon.commit()
    print("Data inserted")

except mysql.connector.Error as err:
    print(err)
finally:
    cursor.close()
    dbcon.close()



fp=open('user.csv','w',newline="")
cw=csv.writer(fp)
cw.writerow(['user_id','name','email','gender'])
cw.writerows(new_users)
print("Data Written Successfully")