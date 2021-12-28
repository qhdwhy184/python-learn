from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        sorted_nums = sorted(nums, reverse=True)
        return sorted_nums[k - 1]


print(Solution().findKthLargest([3,2,1,5,6,4], 2))
print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4))