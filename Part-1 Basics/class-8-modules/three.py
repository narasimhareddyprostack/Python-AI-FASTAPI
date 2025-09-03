import requests

resp=requests.get('https://jsonplaceholder.typicode.com/users')
users=resp.json()

#iterate users using for loop
for user in users:
    print("User Id:",user['id'],"- Name:",user['username'])