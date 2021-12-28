class Item:
    def __init__(self, val, pre=None, next=None):
        self._pre = pre
        self._next = next
        self._val = val

    @property
    def pre(self):
        return self._pre

    @pre.setter
    def pre(self, pre):
        self._pre = pre

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next):
        self._next = next

    @property
    def val(self):
        return self._val

class MinStack:

    def __init__(self):
        self._stack = []
        self._min = None

    def push(self, val: int) -> None:
        pre, next = self._find_pre_and_next(val)
        cur = Item(val, pre, next)

        if pre is not None:
            cur.pre.next = cur
        else:
            self._min = cur

        if next is not None:
            cur.next.pre = cur

        self._stack.append(cur)

    def _find_pre_and_next(self, val):
        if self._min is None:
            return None, None

        i = self._min
        while i.next is not None:
            if i.val < val:
                i = i.next
                continue
            return i.pre, i

        if i.val < val:
            return i, None
        else:
            return i.pre, i

    def pop(self) -> None:
        cur = self._stack.pop(-1)
        if cur.pre is not None:
            cur.pre.next = cur.next
        else:
            self._min = cur.next
        if cur.next is not None:
            cur.next.pre = cur.pre

    def top(self) -> int:
        return self._stack[-1].val

    def getMin(self) -> int:
        return self._min.val

minStack = MinStack()
minStack.push(2)
minStack.push(0)
minStack.push(3)
minStack.push(0)
print(minStack.getMin()) #// return 0
minStack.pop()
print(minStack.getMin()) #// return 0
minStack.pop()
print(minStack.getMin()) #// return 0
minStack.pop()
print(minStack.getMin()) #// return 2


# case 1
# minStack = MinStack()
# minStack.push(-2)
# minStack.push(0)
# minStack.push(-3)
# print(minStack.getMin()) #// return -3
# minStack.pop()
# print(minStack.top())    #// return 0
# print(minStack.getMin()) #// return -2
