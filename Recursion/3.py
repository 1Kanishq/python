def fuct1(a,b,i=0,c=0,c1=0):
    if i>=len(a) and i>=len(b):
        return abs(c-c1)
    if a[i]=='1':
        c+=1
    if b[i]=='1':
        c1+=1
    return fuct1(a,b,i+1,c,c1)
print(fuct1('10011101101','11010001000'))

    
