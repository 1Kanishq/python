# greatest amoung 3 numbers
def funct1(a,b,c):
    if a>b and a>c:
        return "greatest a"
    elif b>c:
        return "greatest b"
    else:
        return "greatest c"
print(funct1(5,8,7))