unames=['rahul','sonai','priyanka',
        'modi','amith','rajni']

def change_case(name):
    return name.upper()

new_users=list(map(change_case,unames))

print(unames)
print(new_users)