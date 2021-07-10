from threading import Thread
from time import sleep


def function_1(a, b):
    sleep(10)
    print('function_1 =', a + b)


def function_2(a, b):
    sleep(2)
    print('function_2 =', a * b)


thread_1 = Thread(target=function_1, args=(2, 3))
thread_1.start()
thread_2 = Thread(target=function_2, args=(2, 3))
thread_2.start()

print('after functions')
