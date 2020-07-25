def foo():
    print("foo - hello")

def eoo():
    print("eoo - hello")

goo = foo

goo()

goo = eoo

goo()