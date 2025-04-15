import random
sides=["east","West","North","South"]
N=random.randint(1,3)
out=''
for i in range(N,1,-1):
    out+=sides[i]
print(out)