# Method Over loading:
class Overload:
    @staticmethod
    def add(a,b):
        return a+b
    prev = add   # Monkey Patching -> 
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
# previous method become waste method
# To restoere the previous method we have a concept called "Monkey Patching"
# Monkey Patching ---> we are storing the address to previous method in new variable. For that method to work we need conept called "Monkey Patching".