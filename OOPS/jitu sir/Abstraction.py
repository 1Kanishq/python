#  Hiding the internal implementaion by providing ,fuctionality to the users is known as abstraction.

# Abstraction
from abc import abstractmethod,ABC
class Animal(ABC): # Abstract class created using ABC 
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):   # Concrete class , the method is override with the help of concrete class by using inheritance
    def sound(self):
        print('Dog Barks')
ob1 = Dog()
ob1.sound()  

class Cat(Animal):
    def sound(self):
        print("meow")
ob2 = Cat()
ob2.sound()