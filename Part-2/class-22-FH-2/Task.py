import requests,json,csv 
response=requests.get('https://jsonplaceholder.typicode.com/users')
users=response.json()
print(response.status_code)
print(type(users))

new_users_json=[]
new_users_csv=[]
for user in users:
    new_users_json.append({"id":user['id'],
                      'name':user['username'],
                      'ciyt':user['address']['city']
                      })
    new_users_csv.append((user['id'],
                          user['username'],
                          user['address']['city'],
                          user['phone']))

#print(new_users_json)
#print(new_users_csv)

fp1=open('users.json','w')
json.dump(new_users_json,fp1)
print("New JSON File created")

fp2=open('users.csv','w',newline='')
csv_writer=csv.writer(fp2)
csv_writer.writerow(['uid','username','city','phoneno'])
csv_writer.writerows(new_users_csv)
print("New CSV File Created")

fp1.close()
fp2.close()