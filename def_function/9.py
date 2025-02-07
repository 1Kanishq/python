# Anagram when the len of str and char is the same
# example: listen --- silent
'''a=input('Enter a string')
b=input('Enter a string')
if len(a)==len(b):
    for i in a:
        for j in b:
            if j in a:'''
'''
def anagram(a,b):
    if len(a)==len(b):
        if sorted(a)==sorted(b):
            print("Its an Anagram")
        else:
            print("Not a Anagram")
    else:
        print("not")

anagram('listed','silent')'''
def fun(a,b):
    if len(a)==len(b):
        for i in a:
            if i not in b:
                print("Its not anagram")
            else:
                print('its a anagram')
    else:
        print("its not")

