import sys



# def huihui(first_arg, *args):
#     print('first_arg:{}'.format(first_arg))
#     print('args:{}'.format(args))
#     print('args[0]:{}'.format(args[0]))
#     f = 1
#     fff = 1
#     key = 'keyname1'
#     plugins = {
#     # talk with owner(Haoran, xiaoyan, Frank Pan) about this, how to add support for esx67
#         '1': 1,
#         '2': 2,
#         '3': 3,
#     }
#
#     copy = plugins.copy()
#     keys = copy.keys()
#     lst = list(keys)
#     st = set(keys)
#
#     print("copy:{}".format(copy))
#     print("keys:{}".format(keys))
#     print("lst:{}".format(lst))
#     print("set:{}".format(st))
#
#     for k,v in copy.items():
#         print("k:{}, v:{}".format(k, v))
#         print("plugins:{} ".format(plugins))
#         print("copy:{} ".format(copy))
#         if k == '2':
#             del plugins['3']
#         print("plugins:{} ".format(plugins))
#         print("copy:{} ".format(copy))



    # new_plugins = plugins.items()
    #
    # print(plugins)
    # print(new_plugins)
    #
    # plugins.pop('2')
    # print(plugins)
    # print(new_plugins)


# huihui(1, 2, 3)


di = {'a':1, 'b': 2}
# di.get("a", True)

di["c"] = "C"
di["f"] = False
print(di)
di.update({'e': 5})
print(di)
# print(type(di))
# print(type(di.keys()))
# print(list(di.keys()))

if 'c' in di:
    print("yes - 'c' in id")
if 'c' in di.keys():
    print("yes - 'c' in di.keys()")

for k, v in di.items():
    print('k:{}, v:{}'.format(k, v))

# print('di["d"]:{}'.format(di["d"]))
# print('di["f"]:{}'.format(di["f"]))
# print("di:{}".format(di))
# di.pop("a", None)
# print("di:{}".format(di))
# di.pop("d", None)
# print("di:{}".format(di))

# print("di['a'].strip():{}".format(di['a'].strip()))
# print("di['c'].strip():{}".format(di['c'].strip()))
# print("di['b'].strip():{}".format(di['b'].strip()))
# print("di.get[\"a\"]:{}".format(di.get("a", None)))
# print("di.get[\"b\"]:{}".format(di.get("b", None)))
# print("di.get[\"d\"]:{}".format(di.get("d", None)))
# print("di.get[\"w\"]:{}".format(di.get("w")))
# print("di.has_key[\"d\"]:{}".format("d" in di))
# print("di.has_key[\"a\"]:{}".format("a" in di))
# print("di[\"a\"]:{}".format(di.get("a")))
# print("di[\"b\"]:{}".format(di["b"]))
# print("di[\"d\"]:{}".format(di["d"]))
# print("di.items():{}".format(di.items()))
# print("di:{}".format(di))


