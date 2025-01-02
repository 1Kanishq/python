# WAP to find the length of substring from the given string in the key value pair of dictionary.
str1 = 'sdcccdcasx'
out=''
i=0
while i<len(str1):
    out+=str1[i]+str(str1.count(str1[i]))
    i+=1
print(out)