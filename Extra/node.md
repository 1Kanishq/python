def means define

def add():    ---> arguments optional
    a = int(input("msg"))
    b = int(input("msg"))
    print(a+b)
add() ---> function call

def add(a,b):    ---> arguments optional
    print(a+b)
add(20,30) ---> function call

return keyword: 


# Recursion works on ---->  runtime stack mechanism

# Generator  
.) Generator is a function which is use to generate sequence of values by the help of 'yield' Keyword
--> If a function contains atleast one 'yeild' keyword inside of it then it is known as generator
.) How to use-->
    'yeild' is a keyword which is used to return n number of values without breaking the flow of execution

.) Generator function always returns a generator object so, to get the required output we have to typecast it.

    Generator function --> generatorobject ---> typecast

.) You can use n no. of yield keywords inside a generators


# Decorators
1. used to add some extra functionality to main function without effecting it.
# decorator is a function which is us to add extra functionality to pur main function without
#  changing/effecting the main function.

        extra functionality ---> main function

2. decorator is a function 

There are 2 types of decorators :
i) In-built decorators  ---> @staticmethod, @classmethod, @abstractmethod

ii) User-defined decorators:

# How to create a decorator

syntax ---> def decorator_name(func):
                def inner(*args,**kwargs): ---> why we are passing this argument,to get n no.of argument
                    [pre_task]
                    func(kargs,**kwargs)
                    [post_task]
                return inner

# How to use decorator
#   @decorator_name
    def func_name(args):
        SB