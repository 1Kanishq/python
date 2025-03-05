# In Python, polymorphisms refer to the occurrence of something in multiple forms.
#  As part of polymorphism, a Python child class has methods with the same name as a parent class method
# Method Over loading: when using multiple methods

class Overload:
    @staticmethod
    def add(a,b):
        return a+b
    prev = add   # Monkey Patching -> 
    @staticmethod
    def add(a,b):
        return(a-b)
    
    @staticmethod
    def add(a,b):    # if monkey patching not done than the last method will be executed instead of whta we want
        return (a*b)
ob1 = Overload()
print(ob1.add(5,6))
print(ob1.prev(5,6))
print(ob1.add(7,3))
print(ob1.prev(7,3))

# Here the latest method is executed , previous method are getting overwrite by latest method.
# previous methods become waste method
# To restoere the previous method we have a concept called "Monkey Patching"
# Monkey Patching ---> we are storing the address to previous method in new variable. 
#                For that method to work ,we need conept called "Monkey Patching".