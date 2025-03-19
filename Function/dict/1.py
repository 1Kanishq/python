# Dictionary function : (values,keys,items,pop,popitem,update,copy,get,setdefault,clear,fromkeys)

# 1-> values()
# dict={1:"hello",2:"Bye",3:"Good"}
# print(dict.values()) #  dict_values(['hello', 'Bye', 'Good'])

# 2-> keys()
# dict={1:"hello",2:"Bye",3:"Good"}
# print(dict.keys()) # dict_keys([1, 2, 3])

# 3-> items()
# dict={1:"hello",2:"Bye",3:"Good"}
# print(dict.items()) # dict_items([(1, 'hello'), (2, 'Bye'), (3, 'Good')])

# 4-> pop() : pop can able to pop any value at any particular key value

# dict={1:"hello",2:"Bye",3:"Good"}
# print(dict.pop(2)) # Bye

# 5-> popitem() : popitem can able to pop the item at the end of the dictionary

# dict={1:"hello",2:"Bye",3:"Good"}
# print(dict.popitem()) # (3, 'Good')

# 6.-> copy() : We can able to make a copy of the sample dictionary

# dict={0:['a','b'],1:['c','d']}
# my_copy=dict.copy()
# print(my_copy) # {0: ['a', 'b'], 1: ['c', 'd']} # This my_copy will have a different address
# changes made in one dict will not affect the other dict, but when we have a nested dict then changes are made in both 

# dict={1:"hello",2:"Bye"}
# dict2=dict.copy()
# print(dict2) # {1: 'hello', 2: 'Bye'}

# 7-> get() : it returns the key values if present otherwise returns none or the default value, and not change the original dict
# dict={1:"hello",2:"Bye"}
# print(dict.get(2)) # Bye
# print(dict.get(45)) # none
# print(dict.get(45,"Yellow")) # yellow
# print(dict.items()) # will not change the orginal dictionary values

# 8. setdefault() : able to get key value pair if that doesn't exist it will create one key value pair
dict={1:"hello",2:"Bye"}
print(dict.setdefault(2)) # Bye 
print(dict.setdefault(5,"yellow"))
print(dict.setdefault(1,"nice"))
print(dict.items()) # dict_items([(1, 'hello'), (2, 'Bye'), (5, 'yellow')])
# can able to change the original dictionary by adding the value it the value doesn't exist in the dict
# but cannot change the existing values inside dict

# 9. clear() : able to clear all the values inside the dictionary
# dict={1:"hello",2:"Bye"}
# dict.clear() 
# print(dict) # {#empty dictionary}

# 10. fromkeys() : the fromkeys() method is used to create a new dictionary with specified keys and a single value assigned to all of them.
#  value is optional and Default value is none
# Syntax: dict.fromkeys(iterable, value) 

# l=[1,2,3,4,5,6]
# # t=(1,2,3,4,5)
# # set={1,2,3,4,5}
# dict1=dict.fromkeys(l)
# print(dict1)

# 11. update() : able to update or modify the dictionary with new key value pairs.
# dict={1:"hello",2:"Yellow",3:"Bye"}
# dict.update({3:"Hello"})
# print(dict)

# How to fectch keys and values
# 1. var[key]
# get() --> It dosen't through any error if the key is not present inside the dict
# keys()---> shows all the keys present
# values()---> shows all the values present
#  items()---> shows all the keyvalue pairs
d = {'a':10,'b':20,'c':100}
d.update({'j':99,'k':36,'i':77}) #We passing keys and values so we have to use {}
print(d)

# setdefault() 
d.setdefault('z')
print(d)
d.setdefault('x',0)
print(d)
d.setdefault('a',200)   # It will not update the existing values
print(d)

# fromkeys() its uses 
