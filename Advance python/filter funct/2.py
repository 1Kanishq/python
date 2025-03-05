# Wap to extract all the pallindrome words from list
list1 = [99,6+3j,'hii',False,'eye','sky',True,'madam']
print(list(filter(lambda n :type(n)==str and n==n[::-1],list1)))

# Wap to extract all the pallindrome Numbers from 1 to 100
palli_num = lambda n: str(n)==str(n)[::-1]

result = filter(palli_num,range(0,101))
print(list(result))

# Wap to extract all the float values which has exactly only 3 values in it.
list2 =[99,False,2.34,6+3j,4.682,'hii',5.447,2.4]
print(list(filter(lambda n : type(n)==float and len(str(n).split('.')[-1])==3,list2)))
# inside lambda -- 1st we check the datatype to be float 
#               -- 2nd we 