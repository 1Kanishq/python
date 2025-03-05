a =10
print('at main space--',a)

def main():
    a+=40   # UnboundLocalError: cannot access local variable 'a' where it is not associated with a value  
    print('Inside the function---',a)
# if we want to access the value of a inside the function we will use global keyword
main()
a+=90
print('After Modification',a)

class Out:

    @staticmethod
    def val():
        print("inside the class--",a)

Out.val()

def main2():
    global
    a+=40   # UnboundLocalError: cannot access local variable 'a' where it is not associated with a value  
    print('Inside the function---',a)
main2()