# WAP to extract all the string value from the list.

list1 = [False,8+5j,'hello',99,'python',8.9,'bye']
def string(list1):
    for i in list1:
        if type(i) == str:
            yield i
var = string(list1)
print(list(var))

# or

print(list(string(list1)))
