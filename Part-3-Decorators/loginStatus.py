def login_req(func):
    def inner(is_login):
        if is_login==False:
            print("Login is Required")
        else:
            return func(is_login)
    return inner