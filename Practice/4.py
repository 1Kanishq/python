a=['hey','hello',10,10+5j,3.4,23,'ab','python']
out=[]
i=0
while i<len(a):
    if type(a[i])==str and len(a[i])>3:
        out.append(a[i])
    i+=1
print(out)