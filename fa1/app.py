from fastapi import FastAPI

#create fastapi app
app=FastAPI()

'''
Usage: Home Page
API URL: http://127.0.0.1:8000/
Method Type:GET
Required Fields: None
Access Type:Public
'''
@app.get("/")
def home_page():
    return {"msg":"Home Page"}

'''
Usage: About Page
API URL: http://127.0.0.1:8000/about
Method Type:GET
Required Fields: None
Access Type:Public
'''
@app.get("/about")
def about_page():
    return {"msg":"About Page"}


'''
Usage: Contact Page
API URL: http://127.0.0.1:8000/contact
Method Type:GET
Required Fields: None
Access Type:Public
'''
@app.get("/contact")
def contact_page():
    return {"msg":"Contact Page"}