# Method Over loading:
class Overload:
    @staticmethod
    def add(a,b):
        return a+b
    
    @staticmethod
    def add(a,b):
        return(a-b)
    
    @staticmethod
    def add(a,b):
        return (a*b)
ob1 = Overload()
print(ob1.add(5,6))
print(ob1.add(7,3))

# Here the latest method is executed , previous method are getting overwrite by latest method.
# previous method 