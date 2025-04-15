# there are 2 types of classes 
# 1. User defined class 2. in-built class  ex- all datatypes

class A:
    pass
ob1 =A()
ob2 = A()
print(type(ob1))
print(type(ob2))

print(id(A))
class B:
    a=10
    b=20
ob3 =B()
ob4 =B()

print('By using class--')
print(B.a)
print(B.b)
print('By Using objects')
print(ob3.a)
print(ob4.a)
ob3.a=40 # Object properties changed 
print(ob3.a)
print(ob4.a)