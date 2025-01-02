#WAP to check the character is upper case or a lowercase or a number or a special character
char = eval(input("Enter the Character"))
if 'A'<=char<='Z':
    print("Uppercase")
elif 'a'<=char<='z':
    print("lowercase")
elif '0'<=char<='9':
    print("Number")
else:
    print("Special cahracter")