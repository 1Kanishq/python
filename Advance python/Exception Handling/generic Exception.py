# When we dont know which type of exception will rise in that case we use Generic Exception Handling,
# In this case we cannot provide specific solution with the exception.
# In generic exception handling we use one class that is exception which contains all the type of errors.
# except KeyboardInterrupt error.

try:
    i=1
    while True:
        print(i)
        i+=1
except Ex:
    print("There are some errors in the code") # No futher statement will execute if keyboarInterrupt (ctrl +c)
 
print ('Further statements of the programe')

# Default Exception Handling
#  in this we can handle all the Exceptions including Keyword Interrupt
# try:
#     Problem Statement
# except:
#     Solution statement