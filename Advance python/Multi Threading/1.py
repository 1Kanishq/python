import threading
from time import sleep
def display(msg):
    for i in range(5):
        print(msg)
        sleep(1)
def other(msg):
    for i in range(5):
        print(msg)
        sleep(1)
t1 =threading.Thread(target=display,args=('Python',)) # We use ,(comma)so that it would be a tuple not string
t2 =threading.Thread(target=other,args=('java',))
t1.start() # To start the Thread
t2.start()
c= threading.current_thread() # Main Thread
for i in range(5):
    print("Hello")
    