# n natural number

# print([i for i in range(int(input("Enter the number: ")))])

# # n natural odd number
# print([i for i in range(int(input("Enter the number: "))) if i%2!=0 ])

# n natural even numbers
# n1=int(input("Enter the number: "))
# var2 =[i for i in range(n1) if i%2==0 ]
# print(var2)

# create list square of even number and cube of odd number

# print([i**2 if i%2==0 else i**3 for i in range(int(input("Enter the number")))])

# s='hai' op[('h',0),('h',1),('h',2),('h',1)]
# print([(i,j) for i in 'hai' for j in range(len('hai'))])

# n=int(input("enter the number "))

# print([i for i in range(1,int(input("Enter the number"))+1) if i%2!=0])

print([i**2 if i%2==0 else i**3 for i in range(0,int(input("Enter the number"))+1)])