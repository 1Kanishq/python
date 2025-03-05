try:
    a = int(input('Enter the number: '))
    b = int(input('Enter the number: '))
    print(a/b)
except ValueError:
    print('The value of a and b should be integer')
except ZeroDivisionError:
    print('The value of b can not be zero')



#  try: