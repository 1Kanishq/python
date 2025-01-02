# WAP to find the greatest number among three numbers
'''a = int(input("Enter the Number a"))
b= int(input("Enter the Number b"))
c = int(input("Enter the Number c"))
if a>b and a>c:
    print("a is the greatest")
elif b>c and b>a:
    print("b is the greatest")
elif c>a and c>b:
    print("c is the greatest")'''

# Other Method
a,b,c,d=eval(input("Enter the numbers"))
if a>b and a>c and a>d:
    print("a is the greatest")
elif b>c and b>d:
    print("b is the greatest")
elif c>d:
    print("c is the greatest")
else:
    print("d is the greatest")