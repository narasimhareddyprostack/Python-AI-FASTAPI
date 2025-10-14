from fastapi import FastAPI
app=FastAPI()

'''
Usage:Application Root Request
API URL:http://127.0.0.1:8000/
Method Type:GET
Required Fields: None
Access Type:Public
'''
@app.get("/")
def home_page():
    return {"message":"Application Root Request"}

'''
Usage:Application About Page
API URL:http://127.0.0.1:8000/about
Method Type:GET
Required Fields: None
Access Type:Public
'''
@app.get("/about")
def about_page():
    return {"message":"About Page"}

users=[
    {'uid':101,'uname':'Rahul','gender':"Male"},
    {'uid':102,'uname':'Sonia','gender':"Femlae"},
    {'uid':103,'uname':'Priyanka','gender':"Female"},
    {'uid':104,'uname':'Modi','gender':"Male"},
]

'''
Usage:Fetch All Users
API URL:http://127.0.0.1:8000/users
Method Type:GET
Required Fields: None
Access Type:Public
'''
@app.get("/users")
def get_users():
    return {"msg":"all user details",'users':users}

'''
Usage:Fetch user by Id
API URL:http://127.0.0.1:8000/users/101
Method Type:GET
Required Fields: None
Access Type:Public
'''
@app.get("/users/{uid}")
def get_user(uid:int):
    print(type(uid))
    for user in users:
        if user['uid']==uid:
            return user 
        
    return {"msg":"User Not exits"}
        
    