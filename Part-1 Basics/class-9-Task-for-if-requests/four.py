import requests
for product in requests.get('https://dummyjson.com/products').json()['products']:
    print(product['title'])
