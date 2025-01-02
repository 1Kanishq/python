
a='abstqz'
op=''
for i in a:
    if i=='z':
        op+='a'
    else:
        op+=str(chr(ord(i)+1))
    
print(op)