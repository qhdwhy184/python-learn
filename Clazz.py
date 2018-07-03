class Parent:
    def __init__(self):
        print("parent - __init__")

class Child (Parent):
    def __init__(self):
        Parent.__init__(self)
        print("Child - __init__")

Child()