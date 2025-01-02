#WAP to Extract all the perfect numbers from 1 -100
out=[]
for i in range(1,101):
    sum=0
    for j in range(1,i):
        if i%j==0:
            sum+=j
    if sum==i:
        out+=[i]
print(out)

    
    