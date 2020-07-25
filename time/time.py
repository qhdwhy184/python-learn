import time
import platform
t1 = time.time()
print('time t1:{}'.format(t1))
time.sleep(1)
# for i in range(1, 10):
#     system = platform.system()
#     time.sleep(100)
#     print(system + str(i))
t2 = time.time()
print('time t2:{}'.format(t2))
print('time consumed:{}'.format(t2 - t1))


t1 = time.time()
print('time t1:{}'.format(t1))
time.sleep(2)
t2 = time.time()
print('time t2:{}'.format(t2))
print('time consumed:{}'.format(t2 - t1))

t1 = time.time()
print('time t1:{}'.format(t1))
time.sleep(3)
t2 = time.time()
print('time t2:{}'.format(t2))
print('time consumed:{}'.format(t2 - t1))