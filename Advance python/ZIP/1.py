# zip
list1=[10,20,30]
list2=[99,88,77]
var=zip(list1,list2)
print(list(var))

#case2
list1=[10,20,30]
s='xyz'
list2=[99,88,77]
var=zip(list1,list2,s)
print(list(var))

#case3
#if we want to iterate 2 collection at a time then we use zip fuction.
for i,j in zip(list1,list2):
    print(i,j)