# Comprehension
# Its a phenomenon of creating a new mutable collection by writing the code in a 
# consice way or by using single line statement

#mut
# There Are 3 types of comprehension:
# --> list comprehension
# --> set comprehension
# --> dict comprehension

# list comprehension --> It is a process of cerating a list by using a single line statement.
#                   Syntax:
                           # var = [val1 for val1 in collection]
                        #   var = [val1 for val1 in collection if condition]

result = [i for i in range(1,20)]
print(result)

var = [i for i in range(1,20) if i%2==0]
print(var)

n1=int(input("enter the number: "))
var1 = [i for i in range(0,n1+1)]
print(var1)