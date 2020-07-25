class Parent:
    # def __init__(self, name):
    #     self._name = name

    def notify(self, msg):
        print("parent notify:{}".format(msg))

    @classmethod
    def print_class(cls):
        print("cls.__name__:{}".format(cls.__name__))

    def self_print_class(self):
        print("self.__class__.__name__:{}".format(self.__class__.__name__))


Parent().print_class()
Parent().self_print_class()