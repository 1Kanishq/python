a=[10,'Hai',3+5j,3210]
out=[]
for i in a:
    sum=0
    if type(i)==int:
        for j in str(i): 
            sum+=int(j)
        out+=[sum]
print(out)