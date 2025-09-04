def user_module(name,status):
    print("user module function started")

    def login():
        print("Login Success")
    def logout():
        print("Logout Success")

    if status == True:
        return login 
    else:
        return logout

inner=user_module('RG',True)
inner() 
