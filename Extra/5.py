# print series of prime number with nested for loop.
# def prime(num):


def prime_no(n):
    ct = 0
    for i in range(1,n+1):
        if n%i == 0:
            ct+=1
    if ct == 2:
        return True
    else:
        return False

for i in range(1,101):
    if prime_no(i) == True:
        print(i,end=" ")