from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for idx in range(0, len(nums) - 1):
            if nums[idx] == nums[idx + 1]:
                return True
        return False

print(Solution().containsDuplicate([1]))
print(Solution().containsDuplicate([1,2]))
print(Solution().containsDuplicate([1,2,3]))
print(Solution().containsDuplicate([1,2,2,3]))
print(Solution().containsDuplicate([1,2,3,3]))
print(Solution().containsDuplicate([1,1,2,3]))
print(Solution().containsDuplicate([1,1,2,2,3]))