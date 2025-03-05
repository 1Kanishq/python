# store the prime number in given range

list1 = [10,'hi',4.5,'Bye',False]
# out =['hi','Bye']

def str_data(n):
    if type(n)== str:
        return True
    else:
        return False
result = filter(str_data,list1)
print(list(result))

# or

def str_data(n):
    return type(n)==str

#or

str_data=lambda n:type(n)==str
result=filter(str_data,list1)
print(list(result))

# or 

print(list(filter(lambda n:type(n)==str,list1)))


