class Arithematic:
    def __init__(self,a):
        self.a = a # memeber
ob1 = Arithematic(10)
print(ob1.a,type(ob1.a))
ob2 =Arithematic(20)
print(ob2.a,type(ob2.a))
print(ob1 + ob2) # TypeError: unsupported operand type(s) for +: 'Arithematic' and 'Arithematic


# class Arithematic:
# Changing the implimentation of parent class method inside the child class method according to the requirement of the child class is known as method overridding