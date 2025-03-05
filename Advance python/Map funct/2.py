# Wap 
s='python is easy'
str_list=s.split()  #['python','is','easy']
def len_word(n):
    return len(n)
list1 = map(len_word,str_list)
print(list(list1))

# or
list1 = map(len,str_list)
print(list(list1))

#or
print(list(map(len,str_list)))

# h ='abc' op- [97,98,99]
h='abc'
print(list(map(ord,h)))

# WAP to get the list of factorial of the n natural number ina given range
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)

n=int(input("enter the num --"))
fact_num = map(fact,range(1,n+1)) # var = map(func_name,colletion)
print(list(fact_num))

s1="python is easy".split()
khuch=list(map(lambda s1:s1[::-1],s1))
print(' '.join(khuch))

