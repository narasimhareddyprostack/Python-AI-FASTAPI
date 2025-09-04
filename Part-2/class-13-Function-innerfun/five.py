def user_module():
    print("outer funciton started")

    def login():
        print("Login Success")

    def logout():
        print("Logout Success") 
    return login

x=user_module()
print(type(x))   #<class 'function'>
#print(x)         #<function user_module.<locals>.login at 0x0000024AD0D3D300>
x()   #Login Success