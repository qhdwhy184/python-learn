from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = None
        summ = None
        for num in nums:
            if summ is None or summ < 0:
                summ = num
            else:
                summ += num
            if res is None or summ > res:
                res = summ
        return res


print(Solution().maxSubArray([2]))
print(Solution().maxSubArray([-1]))
print(Solution().maxSubArray([0]))
print(Solution().maxSubArray([1, -1, 3]))
print(Solution().maxSubArray([-10, 2, -1, 3, 1, -10]))
print(Solution().maxSubArray([10, 2, -1, 3, 1, -10]))
print(Solution().maxSubArray([-10, 2, -1, 3, 1, 10]))
