# List function : (len,append,extend,insert,count,index,remove,pop,reverse,sort,sort(reverse=True),sorted,min,max,sum)

# 1. len() :

# l=[1,2,3,4]
# print(len(l)) # 4

# 2. append() :  It is used to add the data at the last and only accepts single value
# l=[1,2,3,4]
# l.append([10,20])
# print(l) # [1, 2, 3, 4, [10, 20]] # Also update the original list

# l=['hii',True,10]
# l.append([1,2,3]) #['hii', True, 10, [1, 2, 3]]
# print(l)

# 3. Extend() : extend is used when we have to add multiple items 
# l=[1,23,4,5]
# l.extend([10,20])
# print(l) # [1, 23, 4, 5, 10, 20] # Also update the original list , not make list inside the list
# l=['hii',True,10]
# # l.extend(1,2,3) 3 type error, because it always needs a container for multiple values
# l.extend([1,2,3]) # ['hii', True, 10, 1, 2, 3]
# l.extend((1,2,3)) # ['hii', True, 10, 1, 2, 3]
# print(l)

# 4. insert() : It will insert the item at particular index position
# l=[1,2,3,4,5]
# # l.insert(3,30)
# l.insert(0,[1,2,3]) #[[1, 2, 3], 1, 2, 3, 4, 5]
# print(l) # [1, 2, 3, 30, 4, 5]


# 5. count() : it is used to check how many similar items are present inside the list or how many times its repeated.
# l=[1,2,3,4,5,4,1,2,2,1,2]
# print(l.count(1)) # 3
# print(l.count(2)) # 4

# 6. index() : it return the index position of the given element 
# syntax : index(element,start,end)
l=[1,2,3,4,5,2]
print(l.index(2,2) )# 5 


# 7. remove() :
# cannot use remove() like this.
l=[1,2,3,4,4,6]
l.remove(4)
print(l) # Also update the original list

# 8. pop() : able to remove an element from the list by thier index position
# can work as default value pop()
# l=[1,2,3,4,5]
# # l.pop()
# # l.pop(4)
# # l.pop(2)
# last_val=l.pop()
# print(last_val) # 5
# print(l) #[1, 2, 3, 4] #[1,2,4]


# 9. reverse() : reverse the order of the list
# l=[1,2,3,4,5]
# l.reverse()
# print(l) # [5, 4, 3, 2, 1]

# 10. sort() : by default ascending order  with the help of ascii value
# can use only one type of values(homogeneous )
# l=[1,2,5,3,7,2,7,22,74,3]
# l.sort()
# print(l) # [1, 2, 2, 3, 3, 5, 7, 7, 22, 74]
# l.sort()
# l.sort(reverse=True) # able to print our list into reverse order
# print(l)


# 11. sorted(): Take the list as an argument and creates a new list with sorted elements
# l=[1,2,5,3,7,2,7,22,74,3]
# l1=sorted(l)
# print(l1) # [1, 2, 2, 3, 3, 5, 7, 7, 22, 74]

# 12. min(),max(),sum(): not 
# l=[1, 2, 2, 3, 3, 5, 7, 7, 22, 74]
# print(max(l)) # 74
# print(min(l)) # 1
# print(sum(l)) # 126

# 13. clear()

#shalow copy and deep copy

# general copy
list1=[1,2,3,4,5]
list2=list1
print(list2)

list1=[1,2,3,4,5]
new=list1.copy()
print(new) # normal copy

list1=[1,2,3,4,5,]