from fastapi import FastAPI 
from pydantic import BaseModel
app=FastAPI()

users=[]

'''
usage: Fetch all Users
API URL:http://127.0.0.1:8000/users/
Method Type:GET
Required Fields:None
'''
@app.get("/users")
def get_users():
    return users


class User(BaseModel):
    uid:int 
    uname:str 
    loc:str 

'''
usage:create new user
API URL:http://127.0.0.1:8000/users/
Method Type:POST
Required Fields:uid,uname,loc,
'''
@app.post("/users")
def create_user(user:User):
    print(user)
    users.append(user)
    return {"msg":"New User Created","user":user}

