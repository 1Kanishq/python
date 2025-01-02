#WAP to convert all the lower case alphabet to uppercase from the given string
def low(a):
    out=''
    for i in a:
        if 'a'<=i<='z':
            out+=chr(ord(i)-32)
        else:
            out+=i
    return out
print(low('DwadfeaaSAN'))