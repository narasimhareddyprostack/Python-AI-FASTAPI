unames=['rahul','sonai','priyanka',
        'modi','amith','rajni']

new_users=[]
for uname in unames:
    if uname.startswith('r'):
        new_users.append(uname)

print(unames)
print(new_users)