# Wap to extract all the integers from the given text using recurrsion.
def ext_int(a,out=[],i=0):
    if i>=len(a):
        return out
    if type(a[i])==int:
        out+=[a[i]]
    return ext_int(a,out,i+1)
print(ext_int([12,'hello',23,4+3j,[1,2,3],'good']))