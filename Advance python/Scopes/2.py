# a=10
# print('At main space',10)

# def outer():
#     a=100
#     print('Inside the enclosed function--',a)
#     def inner():
#         pass
# outer()
# print('outside',a )


def outer():
    a=100
    print('Inside the enclosed function--',a)
    def inner():
       x=99
       print('Inside the iner function--',x)
    inner()
outer()
print('outside',a)

