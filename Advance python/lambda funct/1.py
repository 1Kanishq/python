# first_name = eval(input("Ente the first name"))
# last_name = eval(input("Ente the last name"))
# var = lambda first_name,last_name: first_name +' '+ last_name
# print(var(first_name,last_name))

# Reverse a number
# num = int(input("Enter the number: "))
# rev = lambda num : str(num)[::-1]
# print(rev(num))

# # Check the number is odd or even:
# # 1.
n=6
# def odd_even(n):
#     if n%2==0:
#         return True
#     else:
#         return False
# #2.
# def odd_even2(n):
#     if n%2==0:
#         return True
#     return False
# #3. 
# def odd_even3(n):
#     return n%2==0
# print(odd_even3)

#4. Or shortest way  is to use lambda function
odd_even4 = lambda n : 'even'if n%2==0 else 'odd'
print(odd_even4(n))

