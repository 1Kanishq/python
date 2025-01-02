# WAP to extract all the pallindrome integers from the given list
a=[121,12321,323,4342]
out=[]
for i in a:
    if not str(i)==str(i)[::-1]:
        continue
    out+=[i]
print(out)
    
        