# Single level ineritance
class A:
    a=10
    b=20
class B(A):
    c="hello"
    a=100

print(A.a,A.b)
print(B.a,B.b,B.c)
