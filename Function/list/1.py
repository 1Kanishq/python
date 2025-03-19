list1 =['hii',12,True]
#list1.extend(1,2,3) # We cant use it it will given TypeError: list.extend() takes exactly one argument (3 given)

# list1.extend([1,2,3]) We have to contain it

list1.insert(0,[1,2,3]) # It also takes single value to insert at a particular position inside the list
print(list1)

# list1.remove() # it takes the specific value to remove that value, it does not have any default value and it will not return the removed value
# list1.pop() # it takes the index value to remove that element, by default it removes last element and it will return the value that is removed 
# sorted() is used for string ,int
last_val=list1.pop(1)
print(last_val)
last_val1=list1.remove(12)
print(last_val1)

sum(list1)

# Tuple we have only two inbuilt fucntion - index(), count()


