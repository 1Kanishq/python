# Multiple inheritance

class Add:
    #@static method
    def add(a,b):
        return a+b
class Mul:
    def mul(a,b):
        return a*b
class Sub:
    def sub(a,b):
        return a-b
class calculator(Add,Mul,Sub):
    def div(a,b):
        return b/a

ob1 = calculator()
calci = ob1
print(calci.add(2,3))
print(calci.mul(2,3))
print(calci.sub(2,3))
print(calci.div(2,3))