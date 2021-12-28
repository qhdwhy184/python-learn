import random


class RandomizedSet(object):

    def __init__(self):
        self.d = {}
        self.i = {}
        self.max_idx = 0

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.d:
            return False
        self.d[val] = self.max_idx
        self.i[self.max_idx] = val
        self.max_idx += 1
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.d:
            return False
        cur_idx = self.d.pop(val)
        self.i.pop(cur_idx)
        if cur_idx != self.max_idx - 1:
            self.i[cur_idx] = self.i[self.max_idx - 1]
            self.d[self.i[cur_idx]] = cur_idx
        self.max_idx -= 1
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        r = random.randint(0, self.max_idx - 1)
        return self.i[r]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(1)
# param_2 = obj.remove(2)
# param_3 = obj.getRandom()
