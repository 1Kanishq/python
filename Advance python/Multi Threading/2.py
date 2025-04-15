import threading
from time import sleep 

class MyThread(threading.Thread):
    def run(self):
        for i in range(1,6):
            print(i)
            sleep(1)
class Aplha(threading.Thread):
    def run(self):
        for i in 'ABCDE':
            print(i,end=" ")
# Object of MyThread class-->
e1 = MyThread()
e2 = Aplha()
e1.start()# To initialize the MyThread
e1.join()
e2.start()# To initialize the Alpha
e2.join()