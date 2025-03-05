# make decorators for mail Qspiders
def mailid(func):
    def inner(*args,**kwargs):
        print("Hello!! candidates glad to see you")
        print("good morning")
        func(*args,**kwargs)
        print('Thanks and ragards')
    return inner

@mailid
def diwali():
    print('wishing U and ur family a happy diwali')
diwali()
