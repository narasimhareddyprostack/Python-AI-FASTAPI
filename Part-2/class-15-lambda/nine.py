numbers=[11,18,31,7,8,232,1055]

def even_nos(num):
    return num%2==0

filter_obj=filter(even_nos,numbers)

even_numbers=list(filter_obj)
print(even_numbers)