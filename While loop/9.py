#WAP to to extract the all the Uppercase alphabet from the given string at even index

# str1 = input('Enter the string')
# out=''
# i=0
# while i<len(str1):
#     if 'A'<=str1[i]<='Z' and i%2==0:
#         out+=str1[i]
#     i+=1
# print(out)
############# Other method
str2= input('enter the string')
out1=''
i=0
while i<(len(str2)):
    if str2[i].isupper():
        out1+=str2[i]
    i+=2
print(out1)