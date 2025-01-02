# wap to extract all the odd numbers from m to n.
n=int(input("Enter the Value of n : "))
m=1
while m<=n:
    if m%2!=0:
        print(m,end=" ")
    m+=1
