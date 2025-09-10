numbers=[11,18,31,7,8,232,1055]

filter_obj=filter(lambda num:num%2 ==0,numbers)
print(list(filter_obj))