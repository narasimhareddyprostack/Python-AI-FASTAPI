import requests,mysql.connector,json,csv 

response_data=requests.get('https://dummyjson.com/users')
user_data=response_data.json()
print(user_data)
users=user_data['users']
print(type(users))
print(len(users))