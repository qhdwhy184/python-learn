def foo(name, *args, **kwargs):
    print("foo- name:{}, args:{}, kwargs:{}".format(name, args, kwargs))
    for a in args:
        print("a in args:{}".format(a))
    for key, value in kwargs.items():
        print("item in kwargs: k:{}, v:{}".format(key, value))
    xoo(name, *args, **kwargs)
    xoo(name, *('a1', 'a2', 'a3'), **{'n2': 'n2', 'n1': 'n1'})


def xoo(name, *args, **kwargs):
    print("xoo- name:{}, args:{}, kwargs:{}".format(name, args, kwargs))
    for a in args:
        print("a in args:{}".format(a))
    for key, value in kwargs.items():
        print("item in kwargs: k:{}, v:{}".format(key, value))


def yoo(name, *args, **kwargs):
    print("yoo- name:{}, args:{}, kwargs:{}".format(name, args, kwargs))
    for a in args:
        print("a in args:{}".format(a))
    for key, value in kwargs.items():
        print("item in kwargs: k:{}, v:{}".format(key, value))
    if 'n1' in kwargs:
        print('Yes, n1 in kwargs, n1:{}'.format(kwargs['n1'] if 'n1' in kwargs else None))
    else:
        print('No, n1 not in kwargs')
    if 'n3' in kwargs:
        print('Yes, n3 in kwargs')
    else:
        print('No, n3 not in kwargs, n3:{}'.format(kwargs['n3'] if 'n3' in kwargs else None))


yoo('hh', n1='n1', n2='n2')


