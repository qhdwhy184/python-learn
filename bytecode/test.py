


n = 0

def foo():
    global n
    n += 1

def voo():
    global n
    n = 1

def boo():
    x = n
    return x

import dis
print('========foo=========')
dis.dis(foo)
print('========voo========')
dis.dis(voo)
print('========boo========')
dis.dis(boo)

print('========print voo========')
print(voo())
