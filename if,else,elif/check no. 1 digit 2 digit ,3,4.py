#WAP to check the number is 1 digit, 2 digit, 3 digit, 4 digit number
num = int(input("Enter the Nmber: "))
if num/1000:
    print("its 4 digit number")
elif num/100:
    print("3 digit number")
elif num/10:
    print("2 digit number")
else:
    print("single digit")