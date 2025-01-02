a='Hai How are you'
op=[]
a.split()
for i in a:
    c=0
    for j in i:
        if j in 'aeiouAEIOU':
            c+=1
    op+=[c]
print(op)
    


