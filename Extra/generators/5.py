# s = eval(input("enter input"))
# def funct(s):
#     for i in s:
#         yield i.lower(),i.upper()
# print(dict(funct(s)))

# # dict 1 ={ 'python':'pn','is':'is,'easy',ey'} 
# s=s.split()
# def dict1(s):
#     for i in s:
#         yield i,i[0]+i[-1]
# print(dict(dict1(s)))

# # dict 2 ={ 'python': '6', 'is':'2', 'easy' : 4}

# def dict2(s):
#     for i in s:
#         yield i,len(i)
# print(dict(dict2(s)))

# # dict 3 ={'python':'nohtyp','is':'si','easy','ysae'}
# def dict3(a):
#     for i in a:
#         yield i,i[::-1]
# print(dict(dict3(s)))
# # dict 4 ={'python':'nythop','is':'si','easy':'yase'}   
# def dict4(a):
#     for i in a:
#         yield i,i[-1]+i[1:-1]+i[0]
# print(dict(dict4(s)))
# dict 5 = {'a97':'A','b98':'B','c99','C'}
a ='abc'
def dict5(a):
    for i in a:
        yield i+str(ord(i)),i.upper()
print(dict(dict5(a)))
