class Upper:
    upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Lower:
    lower_case = 'abcdefghijklmnopqrstuvwxyz'

class Number:
    number = 1,2,3,4,5,6,7,8,9,0

class charcters(Upper,Lower,Number):
    char = '!,#,$,%,^,&,*,(),{},[],?,/' 

print(charcters.upper_case,charcters.lower_case)

