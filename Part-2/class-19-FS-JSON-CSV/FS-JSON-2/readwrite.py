import json 
fp1=open('users.json','r')
fp2=open('employees.json','w')
users=json.load(fp1)
#write users data into new file ie employees.json 
json.dump(users,fp2)
print("New File Json Created!")

fp1.close()
fp2.close()