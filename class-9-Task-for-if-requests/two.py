import requests
resp=requests.get('https://dummyjson.com/products')
product_data=resp.json()
print(resp.status_code)   #200
