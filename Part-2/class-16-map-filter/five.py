unames=['rahul','sonai','priyanka',
        'modi','amith','rajni']

new_users=list(filter(
    lambda name:name.startswith('r'),
    unames
    ))
print(unames)
print(new_users)