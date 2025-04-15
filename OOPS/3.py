# WAp to check the class properties with the objects 
class zoo:
    a='ape'   # Properties of the class
    b='bandar'
    c='crocodile'

kanishq=zoo() # objects of the class
harsh=zoo()

print(zoo.a,zoo.b,zoo.c)
print(kanishq.a,kanishq.b,kanishq.c)
print(harsh.a,harsh.b,harsh.c)

zoo.a='anaconda'
print(zoo.a,zoo.b,zoo.c)
print(kanishq.a,kanishq.b,kanishq.c)
print(harsh.a,harsh.b,harsh.c)

kanishq.b='bhalu'
print(zoo.a,zoo.b,zoo.c)
print(kanishq.a,kanishq.b,kanishq.c)
print(harsh.a,harsh.b,harsh.c)