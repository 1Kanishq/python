#WAP to extarct all the uppercase from the given string

str1='AJDBnSnjsnsnn'
out=''
for i in str1:
    if 'A'<=i<='Z':
        out+=i
print(out)