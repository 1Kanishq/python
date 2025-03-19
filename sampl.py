
a='Python is easy'
# print(a)
# a= a.split()
# print(a)
# # create a function which return odd no in a given range

def odd(n):
   li=[]
   for i in range(1,n+1):
      if i %2!=0:
         li+=[i]
#    print(li)
   return li

print(odd(20)) 



