#WAP to 
a='python is very easy'.split()
out={}
for i in range(len(a)):           # In for Loop if you are dealing with index type questions yuo will use range()
    if int(i)%2==0:
        out[a[i]]= a[i][::-1]+str(len(a[i]))
    else:
        out[a[i]]= len(a[i])*2
print(out)