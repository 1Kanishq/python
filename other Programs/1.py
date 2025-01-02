# WAP to extract all the string present insidde a list whose lenght is greater than 3

a = [10,'heelo',4+5j,3.4,23,'ab','Python']
out=[]
i=0
while i<len(a):
    if type(a[i])==str and len(a[i])>3:
        out+=[a[i]]
    i+=1
print(out)
