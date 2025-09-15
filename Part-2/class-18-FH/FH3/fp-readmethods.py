#read only 42 lines from data.txt

fp=open('data.txt','r')
data=fp.readlines(2)
print(data)