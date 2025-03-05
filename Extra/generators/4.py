def gene():
    print('hello')
    yield True,'hi'
    print('Hii')
    yield (11),(6599)
    
print(dict(gene()))