#WAP to check the no. is divisible by 3 then print fizz if the number is divisible by 5 then print Buzz if the number is 
#divisible by both print FIZZBuzz'''
num = int (input("Enter the NUmber: "))
if num%3==0 and num%5==0:
    print("FIZZBUZZ")
elif num%5==0:
    print("BUZZ")
elif num%3==0:
    print("FIZZ")