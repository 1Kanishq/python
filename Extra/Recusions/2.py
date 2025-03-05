# Wap to print n natural odd numbers
n=10
def odd_num(n):
    if n>0:
        if n%2 != 0:
            print(n)
        odd_num(n-1)
odd_num(n) 

# OR
n=10
def odd_num(n):
    if n>0:
        odd_num(n-1)
        if n%2 != 0:
            print(n)
odd_num(n)
 
