# same function by using the return keyword


def even_odd(num):
    if num%2==0:
        return 'even'
    else :
        return 'odd'

even_odd(20)   # Its will not show the output as it has no container handle the return

print(even_odd(20))

 #or

num = int(input('enter the number'))
