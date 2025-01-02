# a Table for a number

'''num = int(input("Enter a Number"))
i=1
while i<=10:
    print(num ,'x', i ,"=", i*num)
    i+=1
'''
# 791 => 17

num = int(input("Enter the Number"))
sum=0
while num>0:
    ld = num%10
    sum = sum + ld
    num = num//10
print(sum)