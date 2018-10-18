print(' Thread Example')
from time import *
from threading import *

class demo(Thread):
    def run(self):
        for i in range (10):
            print(i)
            sleep(1)

class test(Thread):
    def run(self):
        for i in range (10):
            print('hi')
            sleep(1)


d1 = demo()
t1 = test()


d1.start()
sleep(0.2)
t1.start()


t1.join()
d1.join() # Main Thread will executed after the completion of the t1 thread and d1 thread

print('Main Thread executed after t1 and d1 complete their task ')