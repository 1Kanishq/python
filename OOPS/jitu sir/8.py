# Here we are using Hybrid Inheritance , by combining Single level inheritance 
# In class(Alphabet ,Upper is inherited) and combining multiple inheritance
class Upper:
    @staticmethod
    def upper():
        c1=''
        for i in range(ord('A'),ord('Z')+1):
            c1+=chr(i)
        return c1
class Alphabet(Upper):
    @staticmethod
    def lower():
        c1=''
        for i in range(ord('a'),ord('z')+1):
            c1+=chr(i)
        return c1
class Numbers:
    num=''
    @staticmethod
    def number():
        num=''
        for i in range(10):
            num+=str(i)    
        return num
class character(Alphabet,Numbers):
    def spl_chr():
        sp=''
        for i in range(32,127):  # range of all the characters
            if not chr(i).isalnum():
                sp+=chr(i)
        return sp

print(character.upper())
print(character.lower())
print(character.number())
print(character.spl_chr())
