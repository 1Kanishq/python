# Copy Operation
# It is a process of creating a new variable having the content of old variable
# ---> Ther are 3 types of copy
# 1. General Copy
# --> In this Process the adrees of the existing variable is shared with the ew variable
# ---> If u modify the content of the new variable it will affect the value of the new variable
# Syntax --> new_var=old_var
l1=[10,20,30]
l2=l1
print('list 1---',l1,'addr--',id(l1))
print('list 2---',l2,'addr--',id(l2))
l2[-1]=300
print('After Modifiction')
print('list 1---',l1,'addr--',id(l1))
print('list 2---',l2,'addr--',id(l2))
# 2. Shallow Copy
    # > Here Both the variables have different address 
    # > But the elements present inside the list having the same address
    # > Disadvantages it fails in nested collection as it points to the same address
l1=[10,20,30]# import copy we can import copy module 
l2=l1[::] # or new_var = copy.copy(old_var)
print('list 1---',l1,'addr--',id(l1))
print('list 2---',l2,'addr--',id(l2))
print('After Modifiction')
l2[-1]=300
print('list 1---',l1,'addr--',id(l1))
print('list 2---',l2,'addr--',id(l2))
# 3. Deep Copy
    # > Both the variable will be pointing to the different address 
# > as well as the nested collection present inside the list will point to the different adress
# syntax -- new_var = copy.deepcopy(old_var)
import copy
l1=[10,20,30]# import copy we can import copy module 
l2=copy.deepcopy(l1)
print('list 1---',l1,'addr--',id(l1))
print('list 2---',l2,'addr--',id(l2))
print('After Modifiction')
l2[-1]=300
print('list 1---',l1,'addr--',id(l1))
print('list 2---',l2,'addr--',id(l2))


# create a function inp-we love python ot - ew evol
def rev(a):
    ot=''
    for i in a:
        if i=='':
            ot+=i
        ot+=i[::-1]
    return ot
print(rev('we love python'))
