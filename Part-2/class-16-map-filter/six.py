unames=['rahul','sonai','priyanka',
        'modi','amith','rajni']

def checkname(name):
    return name.startswith('r')

new_users=list(filter(checkname,unames))
print(unames)
print(new_users)