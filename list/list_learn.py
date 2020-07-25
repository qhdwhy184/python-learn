# white = '\033[97m'
# green = '\033[92m'
# red = '\033[91m'
# yellow = '\033[93m'
# end = '\033[0m'
# back = '\033[7;91m'
# info = '\033[93m[!]\033[0m'
# que = '\033[94m[?]\033[0m'
# bad = '\033[91m---\033[0m'
# good = '\033[92m[+]\033[0m'
# run = '\033[97m[~]\033[0m'
#
# l1 = [1, 2, 3]
# print(l1)
# print(l1 + [4])
# string = "string"
# print(l1 + [string])
# print("%s info" % info)
# print("%s good" % good)
# print("%s bad" % bad)


class Obj:
    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return self.val

    def set_val(self, val):
        self.val = val


l1 = [1, 2, 3, Obj('val')]
import copy
l2 = l1.copy()
l3 = copy.deepcopy(l1)

l1[3].set_val('new_val')
print(l1)
print(l2)
print(l3)
print(l1 + [4])
print(l1)
print(l2)
# l1.extend([1, 3])
# print(l1)
