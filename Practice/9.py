a='avsdz'
out=''
for i in range(0,len(a)):
    if a[i]=='z':
        out+='a'
    else:
        out+=chr(ord(a[i])+1)

print(out)
