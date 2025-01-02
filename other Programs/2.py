# Change Lower ,Upper of the string
a = 'hello Kanishq'
out=''
i=0
while i<len(a):
    if 'a'<=a[i]<='z':
        out+=chr(ord(a[i])-32)
    else:
        out+=a[i]
    i+=1

print(out)
