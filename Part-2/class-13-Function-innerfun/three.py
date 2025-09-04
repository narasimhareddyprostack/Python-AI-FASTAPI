def outer():
    print("outer function started")

    def inner():
        print("Inner Function")
    
    inner()
    inner()


outer()
