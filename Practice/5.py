# a= 'How are  you all'
a= 'How are  you all'
out=''
i=0
while i<len(a):
    if a[i]==' ':
        out+='_'
    else:
        out+=a[i]
    i+=1
print(out)