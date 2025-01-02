a=['google.com','Home.py','gamil.com',]
op={}
for i in a:
    a=i.split('.')
    if a[1] not in op:
        op[a[1]]=[a[0]]
    else:
        op[a[1]]+=[a[0]]
print(op)