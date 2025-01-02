
#op
def fun(a):
    out=[]
    for i in range(len(a)):
        if type(a[i])==str and i%2==0:
            out+=[len(a[i])]
        else:
            out+=[a[i]]
    return out
print(fun(['hello',23,3+5j,'python',[1,2,3],34,'star',(1,3)]))