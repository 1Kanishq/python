# for i in range(3):
#     for j in range(3):
#         print('*',end=' ')

# for i in range(3):
#     for j in range(3):
#         print('*',end=' ')
#     print(end='\n')

# n=int(input("Enter the number"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print('*',end=' ')
#     print()
    

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(j,end=' ')
#     print()

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(i,end=' ')
#     print()
# print('='*60)
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()
# print('='*60)

# for i in range(50,56):
#     for j in range(50,i+1):
#         print(j,end=' ')
#     print()

# print('=')
n=5
space =0
for i in range(0,n+1):
    for j in range(0,space):
        print(' ', end=' ')
    for j in range(1,n-space+1):
        print(i+1,end=' ')
    print()
    space+=1