
# Generator  
# .) Generator is a function which is use to generate sequence of values by the help of 'yield' Keyword
# --> If a function contains atleast one 'yeild' keyword inside of it then it is known as generator
# .) How to use-->
#     'yeild' is a keyword which is used to return n number of values without breaking the flow of execution

# .) Generator function always returns a generator object so, to get the required output we have to typecast it.

#     Generator function --> generatorobject ---> typecast

def gene():
    print("Hii")
    yield 10
    print('Hello')
    yield 20
    print('Bye')
    yield 30
var = gene()
print(list(var)) # type casting


def gene():
    print("Hii")
    yield 10,"SQL",True
    print('Hello')
    yield 20,"python"
    print('Bye')
    yield 30,40 # will return in tuple format
var = gene()
print(list(var)) 