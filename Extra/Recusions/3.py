# Sum of n natural numbers

n=5
def sum_num(n):
    if n==0:
        return 0
    else:
        return n + sum_num(n-1) # n value is stored in statck
print(sum_num(n))

# Product

n=5
def prod_num(n):
    if n==0:
        return 1
    else:
        return n * prod_num(n-1)  # n value is stored in stack 
print(prod_num(n))