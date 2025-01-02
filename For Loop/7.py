
a='nitin is a good ava aba'.split()
op=''
for i in a:
    if i==i[::-1]:
        op+=i
        op+=' '
print(op)
