l = []
print(bool(l))
l.insert(0, 0)
l.insert(1, 1)
l.insert(1, 2)
print(bool(l))
print(bool(None))
print(bool(""))
print(bool(" "))
print(bool(0))
print(bool(1))
try:
    assert bool(0) == bool(1)
except Exception as e:
    import traceback

    trace = traceback.format_exc()
    print("Error in main Exception:{}, trace:{}".format(e, trace))

print(l)