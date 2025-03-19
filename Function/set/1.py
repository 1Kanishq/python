# # set functions:(add,update,remove,discard,pop,clear,union(|),intersection(&),difference(-),diffrence_update(),Symmetric_difference,Symmetric_difference_difference_update,issubset,isdisjoint,issuperset)

# # 1. add() : able to add a value iside the set
# # s={1,2,3,4,5,6,7}
# # s.add("hello")

# # print(s) # {1, 2, 3, 4, 5, 6, 7, 'hello'}

# # 2. remove() : able to remove an element from the set but if the remove value is not present in the set it will show error

# # s={1,2,3,45,6}
# # s.remove(3)
# # # s.remove(5) # keyError
# # print(s) # {1, 2, 6, 45}

# # 3. discard() : able to discard an element from the set and also will not show error if element is not present inside the set.
# # s={1,2,3,4,5}
# # s.discard(3) # {1, 2, 4, 5}
# # s.discard(8) # Not Show Error
# # print(s)

# # 4. pop() : pop a random element from set
# # s={1,2,3,4,5}
# # s.pop()
# # s.pop()
# # print(s) #{2, 3, 4, 5}
# # print(s)

# # 5. clear():
# # s={1,2,3,4,5}
# # s.clear()
# # print(s) # set()

# # 6. union(|) : add both set together
# # s1={1,2,3,4}
# # s2={3,4,5,6,7}
# # print(s1.union(s2)) # {1, 2, 3, 4, 5, 6, 7}

# # 7. intersection(&) : similar elements on both the sets
# # s1={1,2,3,4}
# # s2={3,4,5,6,7}
# # print(s1.intersection(s2)) # {3, 4}

# # 8. difference(-) : elements that are not similar in both the sets
# # s1={1,2,3,4}
# # s2={3,4,5,6,7}
# # print(s1.difference(s2)) # {1, 2}
# # print(s2.difference(s1)) # {5, 6, 7}

# # 9. issubset
# # s1={5,6,7}
# # s2={1,2,3,4,5,6,7}
# # print(s2.issubset(s1)) # False
# # print(s1.issubset(s2)) # True

# # 10. issuperset
# # s1={5,6,7}
# # s2={1,2,3,4,5,6,7}
# # print(s2.issuperset(s1)) # True
# # print(s1.issuperset(s2)) # False

# # 11. isdisjoint : if similar elemts are there then --> False , if not then --> True
# # s1={1,2,3}
# # s1={8,9,10}
# # s2={1,2,3,4,5,6,7} 
# # print(s1.isdisjoint(s2)) # False (i)
# # print(s1.isdisjoint(s2)) # True (ii)

# # 12. update()-> use to add multiple value
# s={1,2,3,4}
# print(s.add((12,3,4)))
# print(s.add((True,False)))
# # print(s.add([12,3,4]))

# # print(s.update(1,2.3,'y',[1,2,3],(True,False))) #'int' object is not iterable
# print(s.update(1,2.3,'y',[1,2,3],(True,False)))

s1 = {1,2,3,4}
s2 = {1,2}
print(s1.issubset(s2))
print(s2.issubset(s1))
