
a = 'abadcda'
out=''
for i in a:
    out+=i+str(ord(i)-96)
print(out)