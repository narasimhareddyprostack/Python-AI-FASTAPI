import json 
fp1=open('users.json','r')
fp2=open('employees.json','w')
users=json.load(fp1)
print(len(users))