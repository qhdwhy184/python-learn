import faulthandler
import sys, time, threading,traceback
from threading import Thread



def testexit():
    time.sleep(10)
    print("post thread exit")
    # sys.exit()
    # print("post thread exit")


t = Thread(target=testexit)
t.start()
print("1. sleep")
t.is_alive()
t.start()
print("2. sleep")
t.join()
print("pre main exit, post thread exit")




sys.exit()
print("post main exit")
