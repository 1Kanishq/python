#WAP to check number is even or odd but it should be divisible by 5.
num = int (input("Enter the Number"))
if num%5==0:
    if num%2==0:
        print("Even Number divisible by 5")
    else:
        print("Odd Number divisible by 5")
else:
    print("Not divisible by 5")