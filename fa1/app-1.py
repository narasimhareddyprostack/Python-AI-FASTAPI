from fastapi import FastAPI

#create fastapi app
app=FastAPI()

@app.get("/")
def home_page():
    return {"msg":"Home Page"}

@app.get("/about")
def about_page():
    return {"msg":"About Page"}

@app.get("/contact")
def contact_page():
    return {"msg":"Contact Page"}