# Assertion is a process of throwing an error by assert keyword.

# --> It is a keyword which takes a condition with it
# -->If the condition is false it will throw assertion error with the provided message
# syntax-- assert condition,'msg'

def divide(a,b):
    assert b!=0,'Denominator Should not be zero'
    print(a/b)
divide(10,0)

