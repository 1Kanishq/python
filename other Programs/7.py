
a=[171,23,'Hello',9999,319,'Apple']
i=0
out=[]
'''while i<len(a):
    if type(a[i])== int:
        rev=0
        while a[i]>0:
            ld = a[i]%10
            rev = rev*10 + ld
            a[i] = a[i]//10
        if a[i]==rev:
            out=a[i]
print(out)'''

while i<len(a):
    if type(a[i])==int and str(a[i])==str(a[i])[::-1]:
        out.append(a[i])
    i+=1
print(out)


