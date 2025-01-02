#Wap to extract all the uppercase, lowercase, numbers, special character from your email id.

a="Example123@gamil.com"
i=0
U=''
L=''
N=''
SC=''
while i<len(a):
    if 'A'<=a[i]<='Z':
        U+=a[i]
    elif 'a'<=a[i]<='z':
        L+=a[i]
    elif '0'<=a[i]<='9':
        N+=a[i]
    else:
        SC+=a[i]
    i+=1
print(U,L,N,SC)
