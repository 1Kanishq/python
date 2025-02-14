#Recursion ~~~~
# addition
# list1 = eval(input('Enter a list:'))
# def add_list(list1,length):
#     if length == 0:
#         return 0
#     else:
#         return list1[length-1]+add_list(list1,length-1)
# print(add_list(list1,len(list1)))

# # multiplication
# list2 = eval(input('Enter a list:'))
# def add_list(list2,length):
#     if length == 0:
#         return 1
#     else:
#         return list2[length-1]*add_list(list2,length-1)
# print(add_list(list2,len(list2)))

# Wap to print n natural numbers
n=5
def natural_num(n):
    if n>0:
        natural_num(n-1)
        print(n)
        
natural_num(n)

