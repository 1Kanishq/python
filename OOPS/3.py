# WAp to check the class properties with the objects 
class zoo:
    a='ape'
    b='bandar'
    c='crocodile'

kanishq=zoo()
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