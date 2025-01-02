#WAP to to extract the all the Vowel from the given string
str1=input('Enter the string : ')
out=''
i=0
while i<len(str1):
    if str1[i] in 'AEIOUaeiou':
        out+=str1[i]
    i+=1
print(out)
