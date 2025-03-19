# String : where we can store are character inside "",'',''' '''
# Indexing : when we have a character inside a string then internally those charcter have some index(position value).
# (endswith,startwith,isalpha,isalnum,isnumeric,capitalize,replace,find,count,len,islower,isupper,lower,upper,title,istitle,join,split,isspace)
# 1.
# str="Hello"
# print(str[1]) #Indexing
# print(str[2:6]) # Slicing(starting_index:ending_index)
# print(str[4:]) # [4:len(str)]

# String Functions :

# 1. endswith()
# str="I am coder"
# print(str.endswith("er")) # True

# 2. capitalize()
# str="i am coder"
# print(str.capitalize()) # I am coder # new string created

# 3. replace()
# str="i am coder"
# print(str.replace("i","I")) # I am coder
# print(str.replace("coder","designer")) # i am designer

# 4. find()
# str="i am a coder"
# # print(str.find("a"))  # 2
# print(str.find("coder"))  # 7 - starting index of the word

# 5. count() // count the occurences  of the character in the string.
# str="am i am a coder"
# print(str.count("a")) # 3
# print(str.count("am")) # 2

# 6. Wap to input the first name and print its length
# user=input("Enter the name :")
# print(len(user))

# 7. Wap to find the occurences  of '$' in a string.
# symbol="akjskdh$$m,jk$$jh2324$"
# print(symbol.count("$")) # 5 -> to count the number o time the characetr occurs in the string

