a='Hai Hello'
a=a.split()
out={}
i=0
while i<len(a):
    out[a[i]]=[a[i],len(a[i])*2,a[i][::-1]+str(len(a[i]))]
    i+=1
print(out)
