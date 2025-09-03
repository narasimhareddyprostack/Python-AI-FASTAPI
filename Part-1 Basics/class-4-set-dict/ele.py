product={
    'pid':101,
    'pname':'Marker Pen',
    'price':35.35,
    'details':{
        'color':['Blue','Red','Yellow'],
        'size':"Small",
        'avail':True
    }
}
print(product['details']['color'][0])
print(product['details']['color'][1])
print(product['details']['color'][2])
print(product['details']['size'])