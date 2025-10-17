from fastapi import FastAPI
from pydantic import BaseModel
#create fastapi app
app=FastAPI()

class Product(BaseModel):
    pname:str  
    price:float 
    qty:int 
    info:str 

#Applicaiton Root Req  - http://127.0.0.1:8000/
@app.get("/")
def home_page():
    return {"msg":"Application Root Request"}

'''
API URL: http://127.0.0.1:8000/api 
method Type:POST
'''
@app.post("/api")
def create_product(prod:Product):
    print(prod)
    return {"msg":"New Product Created",'product':prod}