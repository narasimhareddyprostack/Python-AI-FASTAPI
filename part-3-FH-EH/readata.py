fp=None

try:
    fp=open('abc.txt','r')
except FileNotFoundError as err:
    fp=open('default.txt','r')
    print(err)
    data=fp.read()
    print(data)


finally:
    print('finally block execute aways')
    fp.close() 


