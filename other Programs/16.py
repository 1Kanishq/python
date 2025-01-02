'''a = '(())((())'
a1=0
a2=0
i=0
while i<len(a):
    if a[i]=='(':
        a1 = a.count(a[i])
    elif a[i]==')':
        a2 = a.count(a[i])
    i+=1
print(a1-a2)'''
    
   # other method
a = '(())((())'
print(abs(a.count('(')-a.count(')')))