def funct(a,out=[],i=0):
    if i>=len(a):
        return out
    if type(a[i]) is int and a[i]%2==0:
        out+= [a[i]**2]
    else:
        out+=[a[i]]
    return funct(a,out,i+1)
print(funct([2,3.5,7,8,3+5j]))