
a=[10,'Hello',3+5j,[1,2],3.8]
out=[]
for i in a:
    if type(i) in [int,float,complex,bool]: 
        out+=[1]
    else:
        out+=[len(i)]
print(out)