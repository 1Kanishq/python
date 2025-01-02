# Split() Function
#   split is a function which is used for coverting string into a list.

a = 'Python is very easy'.split()
out = {}
i=0
while i<len(a):
    out[a[i]]=a[i][::-1]
    i+=1
print(out)