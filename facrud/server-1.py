from fastapi import FastAPI
app=FastAPI()
#create application root request
#URL:http://127.0.0.1:8000/
@app.get("/")
def home_page():
    return {"msg":"Application Root"}

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
def create_user():
    return {"msg":"New user created"}


'''
Read
----------
Usage:fetch all users
API URL:http://127.0.0.1:8000/read
Method Type:GET
Required Fields:None
Access Type:Public
'''
@app.get('/read')
def get_users():
    return {"msg":"Fetching all users"}


'''
Update
-----------
Usage:update User by Uid
API URL:http://127.0.0.1:8000/update/101
Method Type:PUT
Required Fields:uname,email,mobile
Access Type:Public
'''

@app.put("/update/{uid}")
def update_user(uid:int):
    print(uid)
    return {"msg":"Updating user",'uid':uid}



'''
DELETE
----------------
Usage:delete user by uid
API URL:http://127.0.0.1:8000/delete/101 
Method Type:DELETE
Required Fields:None
Access Type:Public
'''
@app.delete("/delete/{uid}")
def delete_user(uid:int):
    return {"msg":"User Deleted",'uid':uid}