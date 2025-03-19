
# Inheritance
    it is the process of deriving the properties from 1 class to another class
    
    class from which the properties are inherited is known as ---> Parentclass/super class/Base class

    class which inherits the prperties of the parent class or base class is known as ---> Child class/ sub class /derived class.


we have 5 types:-
1) single level inheritance


method resolution order --> malum hai

class add:
    @static method 
    def add(a,b):
        return a+b
class mult

Heirachical inheritance:-

    1 parent class ---------> n no. of child class

                Pc ---->   Cc1 Cc2 Cc3 Cc4.......Ccn
            
    ex: 
        class Pc:
            a = 99
            b = 'python'
        class c1(Pc):
            pass
        class c2(Pc):
            pass

        print(c1.a)
        print(c1.b)
        print(c2.a)
        print(c2.b)

5.) Hybrid inheritance:-
    
    Combination of two or more than 2 types of inheritance 

    A-Z ---> 65-90
    a-z ---> 97-122

    ord('char')
    chr(Ascii value)
# Polymorphism 
     its is the phenomemnon of performing two or more than 2 different operations by the methods or operators
    > its is the process of using the same method or operators in 2 operation or more than 2 differnet operation

    > same methods or operators --------> two or more than two differnent operation

we can explain polymorphism in 3 ways:
    1). Method overloading
    2). Operator overloading
    3). method overriding

# method overloading
     Its the method of using same methods i 2 or more than 2 diff types of operation
     > python does not support method overloading

================================================================================================================


# OOPs
    --> Its is the programming that is based on objects.
    -- > it is use to deal wth realtime program whileworking on the projects oops concept is use..

    --> it basically provide structure to the program.

# Advantages
    -> Modularity -- large projects can be divided into smaller parts.
    -> code reusability
    -> flexibility --
    -> collabration
    -> maintainbility

# class:-
    it is a blue print which contains the properties and functionalities of an object.
    or
    It is a medium where data can be stored & accessed.

# Object:-
->  Instance of the class , Ek hisaa
->  Its a real time entity having some attributes.
->  Object belong to class
->  A class can contain 'n' no. of object.

# Q How to create a class & an object

    class Class_name:   ---- class_name should be capital
            properties/states
            functionalities/behaviours
    obj = Class_name(args)

# Q how to access the data
    class_name.properties
    obj_name.properties

# Q How to modify the properties
1.  By using class

    --->Class_name.property = new property     
    if we r using class for modiing it will affects/modifies the properties for all the object.

2.  By using object
    --->obj.property = new property
    -> if we r using object to modifies  it will afects/modifies the properties for the specific object.

# Types of properties / states / members
> When designing a class in object-oriented programming, the properties (or members) can be categorized based on their scope and behavior. Broadly, they are classified into Class Properties (Static Members) and Object Properties (Instance Members).



    1.) Class / Generic / static

    --> Class properties / class memeber
    -- these are the members of the class which are same or equal for each object

    ex ; if we consider bank as a class who are the class members - who have the account in it  and Bank_name, addr, Branch manager...will be same for every member of the class

    2.) Object / specific / dynamic
    --> object Properties / Object Members: 
    --- These are the members of class different for all the object.

    ex: if we consider bank as a class who are the class members who have the account in it and customer_name ,addr ,accno.,addharno., phno,balance... will be different for every member of the class

# Constructor/init/initialization:
   > It is an inbuilt method which is used to initialize the members of the objects.
     It is use to initialize the members of the objects

   > We dont need to call this method outside of the class, at the time of object creation it get invoked automatically.

   > It is mentatory to pass the 'self' as the 1st argument.('self' carries the address of the object.) 
   
   > we can use other var instead of self but according to the industrial standards we use 'self'.

   > syntax to create constructors;
            class Clss_name:
                def __init__(self,args)
                    self.args = var

# Method/Fuction
    function defined inside a class is known as method.
    
   > Methods are used to provide functionalities to the objects.

   > There are 3 types of methods:
        1. Object method
        2. Class method
        3. Static method
# Object method:
    > Object method r used to Access and modify the object properties.
    > It takes mandatory argument ->'self'
    > To call the object method -> obj.method_name(args)
    syntax to create object method:
        class class_name:
            def method_name(self);
                statement body

# Class method:
    > It is used access & modify the members of the class.
    > It takes a mandatory argument -->'cls' inside of it, which carries the address of the class and object

    '@classmethod' --> useed before defining the class method.

    syntax :-
        class class_name:
            @classmethod
            def method_name(cls,args):
                    SB
        
        class_name.method_name(args)

# Static
> These are niether related to class method nor object method .
> these are used 
> It doesnt take any mandatory argument , It is indepent of object/instance.

> '@staticmethod' -> used before defining the static method

syntax: 
        class Class_name:
            @staticmethod
            def method_name(args):
                    SB
        ob1 = Class_name()

        ob1.method_name(args)
        classname.method_name(args)

        if we want to call this method inside the class method:
            cls.method_name(args)
        if we want to call this method inside the object method:
            self.method_name(args)

# Inheritance:

# Polymorphism
> It is the method of making the same method or operatr to work on two opertions or more than two different tyes of inheritance.

> For example: 
    2+3 ---> (addition)    ,    'hii' + 'bye' ---> (concatination)

Types:
1) > Method Overloading:
        >It is the method of using the same method in 2 or more than 2 different types of operation.
        >In Python Latest method overrides the previous method means it is not possible to perform method overloading in python.
        >However if we want to use the previous methods or waste methods than we have to store the address of the previous method inside the new variable and that new variable which acts as a new method, this process is known as ----> Monkey patching.

2) > Operator Overloading:
        >It is a phenonmen of making the operator to work on the user defined class or user defined datatypes by the  help of ---> magic methods
3) > Method overriding:
        > Changing the implimentation of parent class method inside the child class method according to the requirement of the child class is known as method overridding.
        > to perform method overriding method signature and type of method should be same.
        > method signature = method_name +args

# Encapsulation:
> Wrapping the data and functionality into a single unit.
> It is a process of providing the security to the members of the class by using Access specifiers.

   > Access Specifier:
        > Its specifies whether the user can access the data outside the class or not.
    >There are 3 types of access:
        > 1. Public - These are the members of the class which can be accessible outside the class,
                        Generally what we declare in class by default the are known as public access specifier.

            Syntax:  class Cname:
                        var1 = val1
                        var2 = val2

                        @classmethod
                        def m_name(cls):
                            SB
                        def m_name(self):
                            SB
                        @staticmethod:
                        def mname():
                            SB

> 2. Protected Specifier: These are the members of the class which are to be protected by protacted access specifier
                > To Create protected assecc specifier we have to use the Single Underscore('_') before the members of the class.

        > In Python Protected Access specifier doesn't provide any sequrity or protection to the memebers of the class.

>   3. private Access Specifier :
        > These are the members of the class which cannot be accessed outside the class.
        > To make the class members as Private Access Specifier we have to use Double underscore('__')before the property name  or method name.

        Syntax: Class Parent:
                    __a = 10
                    __b = 20
                    def __cricket(self):
        >                print("Fav player is Kapil dev")
                    ob1= Parent()
                    ob1.a # Can not be accessd 
>   In some situation if User want to access the class member and the method outside of the class than we have to perform following steps:
   > obj/class._Classname__property/method

   > To access or to modify we can use following method also:
    >   get() & set().

# Abstraction: 

> Hiding the internal implementaion by providing ,fuctionality to the users is known as abstraction.
> While designing the project or application the arcitects make use of this abstraction pillar.

> to perform abstraction we required these three things.
    1. Abstract method : This is a method which is declared but not implimented .
                        >'@abstractmethod' is decorator which is used before the declartion of abstraction method.
                            \\=> import  from 'abc' module.
                    Ex:
                        from abc import abstarctmethod
                        class calss_name:
                            @astractmethod
                            def method_name(self,args):
                                pass

    2. Abstract class: if a class contain atleast 1 abstract method than it is known as abstract class.
                    -> it should be child class of 'ABC' class,   ABC = Abstract Base Class
                    -> Object creation is not possible in abstract class.

                    Ex:
                        from abc import abstarctmethod, ABC
                        class class_name(ABC):
                            @astractmethod
                            def method_name(self,args):
                                pass

    3. Concrete Class: If a class doesn't contain any abstract method inside of it then it is known as Concrete class.

    --> In Concrete class object creation is possible.
    --> We will Override the abstract method by providing impelmentaion inside the code.
    --> 

>Polymorphism
It is the method of using same operator or method to perform  two or more than 2 operations. 