import faulthandler
import sys, time, threading,traceback
from threading import Thread

def get_thread_position(thread):
    frame = sys._current_frames().get(thread.ident, None)
    if frame:
        return "f_code. co_filename:{}, f_code.co_name:{}, f_code.co_firstlineno:{}, frame.f_lineno:{}"\
            .format(frame.f_code.co_filename,
                    frame.f_code.co_name,
                    frame.f_code.co_firstlineno,
                    frame.f_lineno)

def testexit():
    time.sleep(10)
    print("post thread exit")
    # sys.exit()
    # print("post thread exit")


t = Thread(target=testexit, daemon=True)
t.start()
# t.join()
print("pre main exit, post thread exit")

t_list = threading.enumerate()
while t_list:
    time.sleep(2)
    t_list = threading.enumerate()
    print("thread count:{}".format(len(t_list)))
    for thread in t_list:
        print("thread name:{}".format(thread.name))
        print("thread position:{}".format(get_thread_position(thread)))
        print("dump:{}".format(faulthandler.dump_traceback()))



sys.exit()
print("post main exit")
