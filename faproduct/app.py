from fastapi import FastAPI
from pydantic import BaseModel,Field,field_validator,ValidationError
#create fastapi app
app=FastAPI()

products=[]
class Product(BaseModel):
    pname:str=Field(...,min_length=3,max_length=40)  
    price:float=Field(...,ge=1000) 
    qty:int=Field(...,ge=1)
    info:str=Field(...) 

    @field_validator('qty')
    @classmethod
    def check_qty(cls,qty:int)->int:
        if qty>100:
            raise ValueError("Qty must be ... Less than 100")
        return qty 

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
    products.append(prod)
    return {"msg":"New Product Created",'product':prod}


#API URL: 
#http://127.0.0.1:8000/api/products
@app.get("/api/products")
def get_products():
    return products