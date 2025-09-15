fp1=open('data.txt','r')
fp2=open('abc.txt','a')

data=fp1.read()
fp2.write(data)
print("New file Created ie abc.txt")