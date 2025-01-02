# WAP to check the is pallindrome

a=input("Enter the String: ")
out=''
i=len(a)-1
while i>=0:
    out+=a[i]
    i-=1
if a==out:
    print("Yes its a pallindrome")
else:
    print("Not a pallindrome")



    
