#WAP to extract all the uppercase from the given string

a='HeLLo'
out=''
for i in a:
    if 'A'<=i<='Z':
        out+=i
    else:
        continue
print(out)
#*************Alternate************
