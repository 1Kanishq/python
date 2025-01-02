n = int(input('Enter the Number : '))
sum = 0
i = 1 
while(i<=n/2):
    if(n%i == 0): 
        sum = sum + i
    i+=1
if(sum==n):
    print('Its a perfect number')
else:
    print("its not a perfect number")