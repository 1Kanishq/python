a="collectionc"
out={}
for i in range(0,len(a)):
    if a[i] not in out and a.count(a[i])>1:
        out[a[i]]=a.count(a[i])
print(out)
