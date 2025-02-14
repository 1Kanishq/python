class Upper:
    @staticmethod
    def upper():
        u=''
        for i in range(ord('A'), ord('Z')+1):
            u+=chr(i)
        return u
    
class Alphabets(Upper):
    @staticmethod
    def lower():
        l=''
        for i in range(ord('a'), ord('z')+1):
            l+=chr(i)
        return l
    
class Numbers:
    @staticmethod
    def number():
        n=''
        for i in range(9):
            n+= str(i)
        return n
class Charcters(Alphabets,Upper,Numbers):  # Multiple inheritance
    @staticmethod
    def spl_char():
        s=''
        for i in range(33,127):
            if not(chr(i).isalnum()):
                s+=chr(i)
        return s
ob1 = Charcters()

print(ob1.upper())
print(ob1.lower())