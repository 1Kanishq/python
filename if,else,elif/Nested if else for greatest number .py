#WAP to check which is greater amoung the 3 number
'''a,b,c=eval(input("Enter the numbers")) 
if a>b:
    if a>c:
        print("A is the greatest")
    else:
        print("C is the greatest")
else:
    if b>c:
        print("B is the greatest")
    else:
        print("C is the greatest")

#### ********************For 5 numbers '''

a,b,c,d,e=eval(input("Enter the numbers")) 
if a>b:
    if a>c:
        if a>d:
            if a>e:
                print("A is the greatest")
            else:
                print("E is the greatest")
        else:
            if d>e:
                print("D is the gratest")
            else:
                print("E is the greatest")
    else:
        if c>d:
            if c>e:
                print("C is the greatest")
            else:
                print("E is the greatest")
        else:
            if d>e:
                print("D is the greatest")
            else:
                print("E is the greatest")
else:
    if b>c:
        if b>d:
            if b<e:
                print("E is the greatest")
            else:
                print("b is the greatest")
        else:
            if d>e:
                print("D is the greatest")
            else:
                print("E is the greatest")
    else:
        if c>d:
            if c>e:
                print("C is the greatest")
            else:
                print("E is the greatest")
        else:
            if d>e:
                print("D is the greatest")
            else:
                print("E is the greatest")