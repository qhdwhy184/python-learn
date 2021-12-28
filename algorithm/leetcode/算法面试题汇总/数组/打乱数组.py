from typing import List
import random


class Solution:

    def __init__(self, nums: List[int]):
        self._nums = nums

    def reset(self) -> List[int]:
        return self._nums

    def shuffle(self) -> List[int]:
        orders = []
        for num in self._nums:
            orders.append((num, random.random()))
        orders = sorted(orders, key=lambda x: x[1])
        res = []
        for item in orders:
            res.append(item[0])
        return res


# Your Solution object will be instantiated and called as such:
nums = [1,2,3,4,5,6]
obj = Solution(nums)
print(obj.shuffle())
print(obj.reset())

nums = [0]
obj = Solution(nums)
print(obj.shuffle())
print(obj.reset())

nums = []
obj = Solution(nums)
print(obj.shuffle())
print(obj.reset())

# param_1 = obj.reset()
# param_2 = obj.shuffle()