#WAP program to print all the factorials from 1 to 10.

for i in range(1,11):
    fact=1
    for j in range(1,i+1):
        fact=fact*j
    print(i,'factorial is : ',fact)