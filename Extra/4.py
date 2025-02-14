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