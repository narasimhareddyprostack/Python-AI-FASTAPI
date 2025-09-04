def user_module():
    print("outer funciton started")

    def login():
        print("Login Success")

    def logout():
        print("Logout Success") 

    return 100

x=user_module()
print(type(x))   #<class 'int'> 
print(x)         #100