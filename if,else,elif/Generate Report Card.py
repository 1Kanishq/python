# WAP to create a student report card
n=int(input("Enter the input"))
if 90<=n<=100:
    print("'A' Grade")
elif 80<=n<=89:
    print("'B' Grade")
elif 70<=n<=79:
    print("'c' Grade")
elif 60<=n<=69:
    print("'d' Grade")
elif n<=59:
    print("'E' Grade")
elif n<=33:
    print("'F' Grade")