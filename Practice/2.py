
'''str1='aabdaccdabc'
out=''
count=1
i=0
while i<len(str1):
    if i<len(str1)-1 and str[i]==str[i+1]:
        count+=1
    else:
        out+=str1[i]+str(count)
        count=1
        i+=1
##print(out)'''
str1= 'aabcdbddaa'
output = ''
count = 1

for i in range(len(str1)):
    if i < len(str1) - 1 and str1[i] == str1[i+1]:
        count += 1
    else:
        output += str1[i] + str(count)
        count = 1

print(output)
