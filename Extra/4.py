def prime(num):
    for i in range(2,num):
        if num%i == 0:
            print('its not a prime')
            break
    else:
        print('its  a prime')
# prime(5)
# prime(20)
# prime(2)
prime(5)
prime(2)

#    Other method

def primeno(n):
    cont = 0
    for i in range(1,n+1):
        if n % i == 0:
            cont += 1
    if cont == 2:
        return 'prime no'
    else :
        return 'not prime'
    