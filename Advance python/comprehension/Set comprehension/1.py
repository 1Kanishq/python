# Store the prime number in a given range.
def prime_no(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True

prime_set = {i for i in range(1,int(input("enter the number "))+1) if prime_no(i)}
print(prime_set)