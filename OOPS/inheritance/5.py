# Multiple inheritance example

class A:
    a=10
    b=20
class B:
    pass
class c:
    d='hello'
    e = "world"
    def __init__(self,a):
        self.a = A
class D(A,B,c):
    f='apple'

print(D.a,D.b,D.d)