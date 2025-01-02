# WAP to calculate the sum of integer substring from the emailId
def intsum():
    E=input("Enter your Email: ")
    summ=0
    for i in E:
        if '0'<=i<='9': # Doubt Why not type(i)==int
            summ+=int(i)
    print(summ)
intsum()