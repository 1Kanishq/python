# 1. Extract all the special characters from a given string
# 2. Return a list containing all the pallindrome numbers from a given range.
# 3. Return  a tuple containg all the prime number in the given range

# # 1
# S = '@9yr2h983'
# def extract_spchar(S):
#     for i in S:
#         if not (i.isalpha() or i.isnumeric()):  # or either use isalnum()
#             yield i   # generator
# var = extract_spchar(S)
# spl_char =''.join(var)
# print(spl_char,type(spl_char))

# # 2
# sv = int(input("Enter the starting value: "))
# ev = int(input("Enter the exit value"))

# def palli_num(sv,ev):
#     for  i in range(sv,ev+1):
#         if str(i)==str(i)[::-1]:
#             yield i
# print(list(palli_num(sv,ev)))


# 3 
def prime_num(n):
    for i in range(2,n):
        ct=0
        for j in range(2,i):
            if i%j==0:
                ct+=1
        if ct==0:
            yield i
        else:
            i+=1
    
print(list(prime_num(20)))




