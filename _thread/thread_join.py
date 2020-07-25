import faulthandler
import sys, time, threading,traceback
from threading import Thread



def testexit():
    time.sleep(1)
    print("post thread exit")
    # sys.exit()
    # print("post thread exit")


t = Thread(target=testexit)
t.start()
print("1. sleep")
time.sleep(5)
print("2. sleep")
t.join()
b = True
b.join()
print("pre main exit, post thread exit")




sys.exit()
print("post main exit")
