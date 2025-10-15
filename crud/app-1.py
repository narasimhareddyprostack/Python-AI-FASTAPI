from fastapi import FastAPI
app=FastAPI()

'''
usage: Application Root Request
API URL:http://127.0.0.1:8000/
Method Type:Get
Required Fields:None
'''
@app.get("/")
def home_page():
    return {'msg':"Application Home Page"}

'''
usage: Fetch all Users
API URL:http://127.0.0.1:8000/users/
Method Type:Get
Required Fields:None
'''
@app.get("/users")
def get_users():
    return {"msg":"Displaying Users"}

'''
usage:Fench - user by Id
API URL:http://127.0.0.1:8000/users/101
Method Type:Get
Required Fields:None
'''

@app.get("/users/{uid}")
def get_user_Id(uid:int):
    return {"message":"Getting user details",'uid':uid} 

'''
usage:create new user
API URL:http://127.0.0.1:8000/users/
Method Type:POST
Required Fields:uid,uname,loc,
'''
@app.post("/users")
def create_user(user:User):
    pass

