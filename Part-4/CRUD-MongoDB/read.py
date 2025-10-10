from pymongo import MongoClient
dbcon=MongoClient('mongodb://localhost:27017/')
db=dbcon['dbone']
product_col=db['products']
products=product_col.find()

for product in products:
    print(product['title'])
