fp1=open("abc.txt",'r')
fp2=open("data.txt","w")

print(fp2.readable())   #False
print(fp2.writable())   #True 
print(fp2.name)         #data.txt
print(fp2.mode)         #w
print(fp2.closed)       #False