# Wap to extract integer from a set.
a={3,2,1,'heelo',3.14}

out=set()
for i in a:
    if type(i)==int:
        out.add(i)
    else:
        continue
print(out)