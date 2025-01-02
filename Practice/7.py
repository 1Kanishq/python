list1=[32,'dddd',45,'dddd',32]
out=[]
i=0
while i<len(list1):
    if list1[i] not in out:
        out.append(list1[i])
    i+=1
print(out)