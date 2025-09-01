import requests
resp = requests.get('https://jsonplaceholder.typicode.com/users')
data=resp.json()
print(type(data))