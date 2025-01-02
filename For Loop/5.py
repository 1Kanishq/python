#WAP to take astring all the uppercase and lowercase 
# if the length of uppercase is more than the length of lowercase print the string as it is.
# otherwise print the concat of uppercase and lowercase

a = input("Enter the string")
out1=''
out2=''
for i in a:
    if 'A'<=i<='Z':
        out1+=i
    else:
        out2+=i
if len(out1)>len(out2):
    print(a)
else:
    print(out1+out2)