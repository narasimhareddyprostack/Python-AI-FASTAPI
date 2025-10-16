from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
users=[]
class User(BaseModel):
    uname:str 
    email:str
    mobile:int 
'''
Create
------------------------
Usage:Create new user
API URL:http://127.0.0.1:8000/create 
Method Type:POST
Required Fields:uname,email,mobile
Access Type:Public 
'''
@app.post("/create")
def create_user(user:User):
    print(user)
    users.append(user)
    return {'msg':"New User Created",'user':user}


'''
Read
----------
Usage:fetch all users
API URL:http://127.0.0.1:8000/read
Method Type:GET
Required Fields:None
Access Type:Public
'''
@app.get("/read")
def get_users():
    return users