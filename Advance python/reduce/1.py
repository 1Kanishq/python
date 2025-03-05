# Reduce()~~~
list1 =[10,20,30,40]
op = 100

add = lambda a,b:a+b
from functools import reduce
var=reduce(add,list1)
print(var)

list2=[22,34,55,42]

greatest = lambda a,b: a if a>b else b
from functools import reduce
var1 = reduce(greatest,list2)
print(var1)

