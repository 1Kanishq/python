a=['google.com','Home.py','gamil.com',]
op=[]
for i in a:
    a=i.split('.')
    op+=[a[1]]
print(op)