import requests,mysql.connector,json,csv 

response_data=requests.get('https://dummyjson.com/users')
users=response_data.json()['users']
print(type(users))
print(len(users))