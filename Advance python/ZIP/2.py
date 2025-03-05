# #Dictionary Comprehension~~~
# #1. WAP to create a dictionary where n natural numbers should act as keys and square of
#     # natural number act as value
# var = {i:i**2 for i in range(int(input("enter the number")))}
# print(var)
# # Wap to map two list collections into dictionary 
# list1 = ['a','b','c']
# list2 = [7,8,9]
# var1 = zip(list1,list2)
# print(var1)

list3 = ['a',8,3.4,[6,7],89]
list4 = [10,3.4,'hello',9,[5,6]]

print({i:j for i,j in zip(list3,list4) if type(i) not in (list,tuple,set)})
#5 
