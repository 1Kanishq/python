a='abacdabacddba'
out=[]
i=0
while i<len(a):
    if a[i] not in out:
        out+=a[i]+str(a.count(a[i]))
    i+=1
print(out)

