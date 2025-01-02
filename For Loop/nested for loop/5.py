a='HaI EverYOne'.split()
out={}
for i in a:
    count=0
    for j in i:
        if 'A'<=j<='Z':
            count+=1
    out[i]=count
print(out)