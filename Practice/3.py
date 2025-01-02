a=273
rev=0
while a>0:
    ld = a%10
    rev=rev*10 + ld
    a=a//10
print(rev)