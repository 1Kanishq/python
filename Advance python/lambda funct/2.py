# Check the given data is mutabable or immutable:

data = eval(input("Enter the data  "))
result = lambda data : 'Mutable'if type(data) in (set,dict,list) else 'immutable'
print(result(data))

# WAP to find the sum of maximum of 5 numbers and minimum 2 numbers by using lambda
summ = lambda a,b,c=0,d=0,e=0: a+b+c+d+e
print(summ(20,3))