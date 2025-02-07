# Multi level inheritance

class A:
    a = 12
    b = 20
class B(A):
    c=30
    d=14
class C(B):
    pass

print(A.a,A.b)
print(B.a,B.b,B.c,B.d)
print(C.a,C.b,C.c,C.d)