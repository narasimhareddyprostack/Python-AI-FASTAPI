numbers=[10,20,30,40]

def addplusone(num):
    return num+1

map_obj=map(addplusone,numbers)
new_numbers=list(map_obj)
print(new_numbers)