def user_module():
    print("outer funciton started")

    def login():
        print("Login Success")

    def logout():
        print("Logout Success") 
    return login

inner=user_module()
print(type(inner))   #<class 'function'>
inner()              #Login Success
inner()              #Login Success
inner()              #Login Success