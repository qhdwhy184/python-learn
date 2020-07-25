import os
lname = __name__
class Plugin:
    def p_id(self):
        print('p_id:{}'.format(id(self)))
    def test(self):
        print('Plugin.__'
              'name__:{}'.format(Plugin.__name__))

    def test2(self):
        print('Plugin.__name__:{}'.format(self.__class__.__name__))

    @classmethod
    def test3(cls):
        print('Plugin.__name__:{}'.format(cls.__class__.__name__))

p = Plugin()
p.test()
p.test2()
p.p_id()
Plugin.test3()
print('lname:{}'.format(lname))

# Path 
# path = "/home"
# print("start")
# # Join various path components
# print(os.path.join(path, "User/Desktop", "file.txt"))
# print("path:{}".format(path))
# print("os.path.join(path):{}".format(os.path.join(path)))
# print("os.path.basename(/home/User/Desktop/file.txt):{}".format(os.path.basename("/home/User/Desktop/file.txt")))


# # Path
# path = "User/Documents"
#
# # Join various path components
# print(os.path.join(path, "/home", "file.txt"))
#
# # In above example '/home'
# # represents an absolute path
# # so all previous components i.e User / Documents
# # are thrown away and joining continues
# # from the absolute path component i.e / home.
#
#
# # Path
# path = "/User"
#
# # Join various path components
# print(os.path.join(path, "Downloads", "file.txt", "/home"))
#
# # In above example '/User' and '/home'
# # both represents an absolute path
# # but '/home' is the last value
# # so all previous components before '/home'
# # will be discarded and joining will
# # continue from '/home'
#
# # Path
# path = "/home"
#
# # Join various path components
# print(os.path.join(path, "User/Public/", "Documents", ""))