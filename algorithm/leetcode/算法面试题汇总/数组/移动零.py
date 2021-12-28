from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        zero_idx = self.find_zero_idx(0, nums)
        if zero_idx is None:
            return


        non_zero_idx = self.find_non_zero_idx(zero_idx, nums)

        if non_zero_idx is None:
            return

        if zero_idx > non_zero_idx:
            return

        while non_zero_idx is not None:
            nums[zero_idx] = nums[non_zero_idx]
            nums[non_zero_idx] = 0
            non_zero_idx = self.find_non_zero_idx(non_zero_idx + 1, nums)
            zero_idx = self.find_zero_idx(zero_idx + 1, nums)

    def find_zero_idx(self, begin_idx, nums):
        for idx in range(begin_idx, len(nums)):
            if nums[idx] == 0:
                return idx
        return None

    def find_non_zero_idx(self, begin_idx, nums):
        for idx in range(begin_idx, len(nums)):
            if nums[idx] != 0:
                return idx
        return None

nums = [1, 2, 3]
Solution().moveZeroes(nums)
print(nums)
nums = [1, 0, 2, 3]
Solution().moveZeroes(nums)
print(nums)
nums = [0, 1, 2, 3]
Solution().moveZeroes(nums)
print(nums)
nums = [1, 2, 3, 0]
Solution().moveZeroes(nums)
print(nums)
nums = [1, 0, 0, 2, 3]
Solution().moveZeroes(nums)
print(nums)
nums = [0]
Solution().moveZeroes(nums)
print(nums)
nums = [1]
Solution().moveZeroes(nums)
print(nums)