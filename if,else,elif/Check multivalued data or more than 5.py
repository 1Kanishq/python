#To check a program is multivalued data type else the value is more than 5
data = eval(input("Enter the data "))
if isinstance(data,(tuple,dict,set,str,list)) and len(data)>5:
    print("multi valued")
else:
    print("Not multi valued")