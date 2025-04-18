## Type Casting in Python
Type casting (or type conversion) in Python is the process of converting one data type into another. Python provides two types of type conversion:

✅ 1. Implicit Type Conversion (Automatic Conversion)
Python automatically converts one data type to another without user involvement.

This happens when performing operations between different types.

🔥 Example:
# Integer to Float
a = 5
b = 2.5
result = a + b  # int + float -> float
print(result)    # Output: 7.5
print(type(result))  # Output: <class 'float'>
💡 When does implicit conversion occur?
Integer to Float

Integer/Float to Complex

Boolean to Integer or Float

✅ 2. Explicit Type Conversion (Type Casting by User)
Explicit type conversion is done manually using predefined functions.

🔥 Common Type Casting Functions
Function	Description	Example
int(x)	Converts x to an integer	int(5.6) → 5
float(x)	Converts x to a float	float(5) → 5.0
str(x)	Converts x to a string	str(10) → '10'
bool(x)	Converts x to a boolean	bool(0) → False
list(x)	Converts x to a list	list('abc') → ['a', 'b', 'c']
tuple(x)	Converts x to a tuple	tuple([1, 2]) → (1, 2)
set(x)	Converts x to a set	set([1, 2, 2]) → {1, 2}
dict(x)	Converts x to a dictionary	dict([(1, 'a'), (2, 'b')]) → {1: 'a', 2: 'b'}
 
# Sort Function
 its the function used for arranging items.
 either in ascending or decending order.
 Sort is an inbuilt function which is used to convert a number list into acsending order

Syntax:-
    variable.sort() 

# Split() Function
    split is a function which is used for coverting string into a list.

# count()
    It is an inbuilt function in python which is use to count number iof substring of the main string.
    Syntax:
        var.count("Substring")

# For LOOP
    same set of instruction again and again unless the condition become false
    But For loop depends on the collection

    syntax:
        for i in collection:
                            collection can be Range, str, list,tuple,set, dict
    
    In for loop we dont hae to intialze, update the collection it autoaticlly get updated
# range()
    range is a inbuilt function which is used to set the flow of collection by lower, upperlimit
    syntax: 
            range(startingpoint,endingpoint,step)

    whenever we deals with number we use range function.

# continue()
    ✔ continue is a keyword which is used to skip the iteration without breaking the loop.
    ✔ In this process we dont put any conditions on continue.
    ✔ It will work for for loop, while loop both.

for i in range()


# pass
    it is a keyword which make empty block as a valid block

# Intermediate terminating loop:
    These are the loops where it come out of thee loop unfortunstely at a given instance
    using some key words this phenomenon is known as temination loop

    this process is unpredictable it can work any time.

    1. Break
    2. Continue
    3. Pass

    Break is a keyword which eliminate the loop at a single point where controler come out 
    of the loop and it cant go back
        syntax:
                break
        example:
            for i in range(1,11):
                if i ==5:
                    break
                print(i)
# Nested for loop:
    These are the for loop where same set of instructions are done again and again until and unless the condition become false but ths loop contains
    a loop inside a loop in the form of for loop where the inner loop is dependent on the outerloop.

    syntax: 
        for var in collection:
            for var in collection:

# Cpitalize()
    Is an inbuild function which is use to convert the first letter of the string into uppercase.
#def 


1-> static member

# Sum inbuilt function
    1) isalpha() ---> forchecking list contain alphabets (UPPER and lower both)
    2) isnumeric() ---> for checking list contain numbers
    3) isalnum() ---> for checking list contains alphanumeric 

# Format string/f-string

    > multiple variable substitution

    ex: print(f"str{var1}str{var2}str.....{varn}")

# def add(a,b):
    print('hi')
  add(20,10)



# Scope:
> It refers to the region of module where we can write(modify) and read(access) the values of the variable.

> LEGB rule

L-> Local Scope
E-> Enclosed / non-local scope 
G-> Global Scope
B-> Built in Scope

> Built-in Scope :
    The utility function like len(),input(),type() are belong to built in scope of variable.

    we can access these inside of any model without importing it

> Global Scope:
    These are the variable which is declared at the main space of a module or outside of the class or a function.

    we can access these variable inside the main space ,inside the class and inside the function.

    we can modify the global scope in main space only.

    example:
            a =10
            print('At Main space',a)
            def main():
                print('inside the function--',a)

> Enclosed / non-local :
    These are the variables declared inside a enclosed fucntion

    The lifespan of that variable remains inside of that function only.

    we can access that variable inside the function only.

    example: 
            a=10
            print('At main space',10)

            def outer():
                a=100
                print('Inside the enclosed function--',a)
                def inner():
                    pass
            outer()
            print('outside )

>Local Scope:
    
    If we declare any variable inside a fucntion then it wil be known as local scope

    example:
        a=5  <----------Global Scope
        def outer():
            a=10 <-------Enclosed / non-local scope
            def inner():
                a=100 <---------local scope

# Functions in Python

## Overview
Functions in Python are reusable blocks of code that perform a specific task. They help in organizing code, making it more readable, and avoiding repetition.

## Types of Functions
1. **Built-in Functions** – Predefined functions like `print()`, `len()`, `type()`, `sum()`, etc.
2. **User-defined Functions** – Functions created by the user using the `def` keyword.

## Creating a Function
A function is defined using the `def` keyword.

### Syntax:
```python
def function_name(parameters):
    """Optional docstring"""
    # Function body
    return value  # (optional)
```

## Example of a Simple Function
```python
def greet():
    print("Hello, World!")

greet()  # Output: Hello, World!
```

## Function with Parameters
```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8
```

## Function with Default Parameters
```python
def greet(name="User"):
    print(f"Hello, {name}!")

greet()        # Output: Hello, User!
greet("Alice") # Output: Hello, Alice!
```

## Lambda Function (Anonymous Function)
```python
square = lambda x: x * x
print(square(4))  # Output: 16