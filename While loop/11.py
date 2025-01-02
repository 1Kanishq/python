#WAP to extract the Uppercase Characters from the given strings, concatenated with its length.
str1 = input("Enter the String : ")
out=''
i=0
while i<len(str1):
    if 'A'<=str1[i]<='Z':
        out+=(str1[i])
    i+=1
print(out + str(len(out)))