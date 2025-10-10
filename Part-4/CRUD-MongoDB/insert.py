from pymongo import MongoClient

dbcon=MongoClient('mongodb://localhost:27017/')
db=dbcon['dbone']
user_col=db['users']
user_col.insert_one({"uid":101,"uname":"Rahul"})
print("Data inserted successfully")
