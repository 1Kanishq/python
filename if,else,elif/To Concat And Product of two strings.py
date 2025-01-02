# WAP to print concact of 2 strings if length of 1st string is greater than length of 2nd string if not
#print the product of first string with length of second string
string1 = input("Enter the String")
string2 = input("Enter the 2nd String")
if len(string1)>=len(string2):
    print(string1+string2)
else:
    print(string1*len(string2))
    