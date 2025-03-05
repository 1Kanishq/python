# decorator is a function which is us to add extra functionality to pur main function without
#  changing/effecting the main function.

def instagram(func):
    def inner(*args,**kwargs):
        print("www.instagram.com")
        print("Login done")
        func(*args,**kwargs)
        print("logged out")
    return inner


def kanishq():
    print("Watching Reels")
kanishq()

print('='*40)

@instagram
def kanishq():
    print("Watching Reels")
kanishq()

print('='*40)
@instagram
def mohit():
    print("messaging")
mohit()

