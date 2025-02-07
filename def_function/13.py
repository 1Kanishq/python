# function with return and with argument
# WAP Uper to lower  and lower to uper using this function 

def funct(a):
    out=''
    for i in a:
        if 'a'<=i<='z':
            out+=chr(ord(i)-32)
        else:
            out+=chr(ord(i)+32)
    return out
print(funct('AUIFDbcbdbUdbsbudb'))
    