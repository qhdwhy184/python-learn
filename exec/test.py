
import importlib
import os
import sys
import traceback
import importlib.util
import time
import uuid

sys.path
sys.getsizeof
sys.getrefcount
sys.maxsize

default_global = {
    'sys_path': sys.path,
    'sys_getsizeof': sys.getsizeof,
    'sys_getrefcount': sys.getrefcount,
    'sys_maxsize': sys.maxsize,
    'sys_getrecursionlimit': sys.getrecursionlimit,
    # 'hello_world': hello_world,
    # 'hello_world_no': hello_world_no
}

plugin_path = os.path.join(os.path.dirname(__file__), "script.py")

# print(plugin_path)
with open(plugin_path, 'r') as f:
    try:
        file = f.read()
        exec(file, default_global)
    except Exception:
        trace = traceback.format_exc()
        print("trace:{}".format(trace))
