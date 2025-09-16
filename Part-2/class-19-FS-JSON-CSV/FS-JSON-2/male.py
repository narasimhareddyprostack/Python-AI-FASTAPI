import json 
fp1=open('users.json','r')
fp2=open("male.json",'w')

users=json.load(fp1)

male_users=[]
for user in users:
    if user['gender']=="Male":
        male_users.append(user)

print(len(male_users))
json.dump(male_users,fp2)

print("New Json File created")
fp1.close()
fp2.close()