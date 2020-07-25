import traceback


def foo():
    print("h1")
    raise Exception("test ex")
    print("h2")


def too():
    try:
        foo()
    except Exception as e:
        str = traceback.format_exc()
        print("str trace: %s" % str)
        print("e: %s" % e)
        print( e)


too()
