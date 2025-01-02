# WAp to extrat all the Uppercase character from the given string

a = 'jkvhsuhAddfhfhsdDWdd'
i=0 
out=''
while i<len(a):
    if 'A'<=a[i]<='Z':
        out+=a[i]
    i+=1
print(out)