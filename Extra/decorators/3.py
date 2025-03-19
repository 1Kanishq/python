import time
start =time.time()
# print("start time",start)
# for i in range(0,50):
#     print(i)
end =time.time()
# print("Ending time : ",end)
# print('Total time taken is : ',end-start)

# Create a dcorator to calculate the total time taken to execute any programme

def dec_time(func):
    def inner(*args,**kwargs):
        print("starting time is : ",start)
        func(*args,**kwargs)
        print("ending time",end)
        print("Total time taken: ",end-start)
    return inner

@dec_time
def loop():
    for i in range(0,100):
        print(i)
loop()   # loop = decorator_name(loop\\
d

@dec_time
def whileloop():
    i=0
    while i<100:
        print(i)
        i+=1
whileloop()