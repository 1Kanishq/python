#WAP a program to sum all the digits of a number.
num = int(input("Enter a Number: "))
sum=0
while num>0:
    Ld= num%10
    sum = sum + Ld
    num = num//10
print(sum)