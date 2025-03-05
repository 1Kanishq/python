class Arithmetic:
    def __init__(self,a):
        self.a=a
    def __add__(self,other): #magic method
        return self.a+other.a
    def __sub__(self,other): #magic method
        return self.a-other.a
ob1=Arithmetic(20)
ob2=Arithmetic(10)

print(ob1+ob2)
# print(ob1.a+ob2.a)
