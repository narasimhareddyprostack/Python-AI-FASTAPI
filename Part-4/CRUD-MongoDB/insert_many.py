import requests,pymongo
#extract data from rest api
response_data=requests.get('https://dummyjson.com/products')
product_data=response_data.json()
products=product_data['products']
print(len(products))
#tranform data
beauty_products=[]
for product in products:
    if product['category']=='beauty':
        beauty_products.append(product)
print(len(beauty_products))
#load into mongodb collection
dbcon=pymongo.MongoClient('mongodb://localhost:27017/')
db=dbcon['dbone']
product_col=db['products']
product_col.f
product_col.insert_many(beauty_products)
print("Data Inserted successfully")