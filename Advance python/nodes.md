# var = lambda args : expression

var()

# WAP to concatenate the first name & sirname of the user

# Reverse a number

# Map Function

Map is a inbuilt function which is used to traverse through the inbuilt collection
to perform same task onn each and every value on the same task

---> the lenght of the input = length of the output

    syntax:  var = map(func_name,collection)
            print(list(var))
     # it takes function as as anrgument thats why known as

Two arguments
i) func_name
ii) iterable datatype or collection data type

this variable returns a map object so to get the required output we have to typecast it

# Filter():

    Filter function is an inbuilt function which is use to traverse the values present in the collection

    traverse through the collection ---> S

    Length of the output collection maybe equal or less than the input collection.

# syntax(): var = filter(fname, Collection/iterable datatype)

# print(list(var))

# why we call filter , Map , reduce as in it we give function as an argument

# reduce():

1.  Its is an in build function which is used to reduce our itreable datatype into a single unit.
2.  It uses a mathemathical folding technique.
3.  To use the reduce fucntion we have to import the " functools" modules.
4.  syntax: var = reduce(f_name, collection)
    print(var) => no need for type casting.

# Comprehension 
> It is the process of creating new collection by writing the code in a concise manner.
>It is a phenomemno of creating consice fucntion, concise way of writing the code to create a new mutable   collection.
> There are 3 types of comprehension, --> list comprehension, set Comprehension , dictionary comprehension

> list Comprehension-  it is a process of creating a new list by using a single line of code

    var = [val1 for val1 in collection] ==> General syntax
    var = [val1 for val1 in collection if condition] ==> when 1 SB
    var = [val1 if condition else val2 for val1 in collection] ==> when 2 SB
    var = [(val1,val2) for val1 in collection for val2 in collection ] ===> nested for loop.

# set Comprehension:

    >It is a phenomemnon of creating a set by using a single line of statement.

    syntax:
    var = {val1 for val1 in collection} ==> General syntax
    var = {val1 for val1 in collection if condition} ==> when 1 SB
    var = {val1 if condition else val2 for val1 in collection} ==> when 2 SB
    var = {(val1,val2) for val1 in collection for val2 in collection} ===> nested for loop.

# zip():

    > It is use to combine 2 or more, differnt iterables into a single iterable
      W.R.T index position

    > It creates a tuple to store the zipped elements
    > It always consider the collection having shortest length
    > #zip() function always return some zip object so we have to typecast it.
        syntax():
                var = zip(collection1,col2,col3....colln) ->> typecast the var --> print(list(var))

if we want to iterate 2 collection at a time then we use zip fuction.

# Dictionary Comprehension: 

var = {k:v for val1 in collection}
var = {k:v for val1 in collection if (coll1,coll2)}
var= {k:v for val1 in collection if condition}
var= {k:v v1 if condition else v2 for val in collection }

# Regular Expression:

> It is the process of writing a pattern to filter the data from a huge data that is nothing but string.
> RE- Module (re stands for rgular) ---------------------------->>>>
> .findall -> fetch al the data
> Syntax:
> import re
> var = re.findall('pattern',data/var)

# Difference between package and module

> Package:

    1.It is a folder which contains n number of modules inside a function.
    Example:
    ---> Numpy, Pandas ,metplotlib, django etc.
    # Installation is required.
    --> pip install Package name

> Module:

1.  Module is a file which contains n number of instructions/methods
    Example:
    ---> keyword , math, time, random, copy, functools, re

    > Need to import the module
    > ---> import module_name

There are 2 types of modules:

1. In-Built module
2. Built-in module

> how to access the modules:

1. by using import: It gets all the methods present inside the module. syntax(import module_name),
        module_name.method_name(args) , get all the methods takes more memory .
2. by using from : > syntax( from module_name import method1, method2, ...., method n), to use --> method_name(args)
3. by using *:  > from module_name import* ---> method name

# File handling
> File is a container which contains the data.
> By the help of the extensions we can know which type of the data is stored inside a file.

> It is the process o writiing the data into the file or reading the data from the file.
> To perform file handling first we need the access of that file.

<!-- To Access The File-->

> var = Open('file name.exe/loc', 'mode') 
    mode => types of operation we want to perform on the file.
    > There are three types of modes write mode, read mode and append mode.

> 1. write mode (w): it is used to write the data inside the file, denoted by 'w'
    > File exist: It will override that file.
    > Dosen't exist: Then it will create a new file.
    > i) write():-
        > Used to write single line of data
    > ii) writelines():-
        > used to write multiple lines of data.
            data1 = 'str1'
            data2 = 'str2'
            data3 = 'str3'
    > iii) Close():
        > used to save the data inside the file.
        syntax: var.close()

> 2. read mode(r): it is used to read the data from the file, denoted by 'r'
        > File Exist--> read the data
        > Does't Exist ---> throw error
        > Default mode
    > i) read():-
        > Get entire content of the file.
        syntax : data = var.read()
    > ii) readline():-
        > read one line of statement at a time
        syntax : data = var.readline()
    > iii) readlines():-
        > read all the lines from the file.
        > return a list containing all the lines as substring.
        syntax : data = var.readlines()
> 3. Append mode('a'):- In this mode it will not overwrite the previous data instead add the new data with the existing data. 

# CSV file:
> It is a file where the data is stored with seperated of comma.
> in real time appliction data stored in csv file.
# How to wite the data into csv file.
> import csv
> var = open('file_name.exe/loc,'w')
> a = csv.writer(var)

1. writerow(): Its is used to wirte single row inside the file in the form of list.
    > ex - a.writerow([data1,data2,....datan])
2. writerows(): multiple rows at a time in the form of list.
    > ex - a.writerows([[data1,...],[data1,...],[data1,...]])

# Exception Handling
> When we dont know which type of exception will rise in that case we use Generic Exception Handling,
 >In this case we cannot provide specific solution with the exception.
 >In generic exception handling we use one class that is exception which contains all the type of errors.
 >except KeyboardInterrupt error.
  Syntax:    try:
                Problem statement
             except Exception:
                solution statement

# Customised Exception
 > Python supports the user to through exception according to its requirement.
syntax: raise ErrorName('msg')

> User Defined Exceptions 
 > These Are the exception that aare defined by the user.

 syntax:    class AgeError(Exception):
                    pass
            Then Call it with the help of raise error