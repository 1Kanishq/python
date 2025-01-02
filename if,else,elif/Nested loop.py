#WAP to check the character is vowel or consonent but with nestedif
char = eval(input("Enter the character"))
if 'a'<=char<='z' or 'A'<=char<='Z':
   if char in 'aeiouAEIOU':
      print("Its a Vowel")
   else:
      print("not a Vowel")
else:
   print("Invalid")
               