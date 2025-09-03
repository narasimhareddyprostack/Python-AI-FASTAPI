import requests
resp=requests.get('https://dummyjson.com/products')
product_data=resp.json()
products=product_data['products']
print(type(products))  #list
print(len(products))   #30


for product in products:
    print(product['title'])
