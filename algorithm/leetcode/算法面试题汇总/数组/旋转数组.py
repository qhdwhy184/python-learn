from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = nums.copy()
        for idx in range(0, len(res)):
            target_idx = (idx + k) % len(res)
            nums[target_idx] = res[idx]


nums = [1, 2, 3]
k = 1
Solution().rotate(nums, k)
print(nums)
nums = [1, 2, 3]
k = 0
Solution().rotate(nums, k)
print(nums)
nums = [1, 2, 3]
k = 3
Solution().rotate(nums, k)
print(nums)
nums = [1]
k = 3
Solution().rotate(nums, k)
print(nums)
nums = [1, 2]
k = 3
Solution().rotate(nums, k)
print(nums)

# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         while k > 0:
#             self.rotate_one(nums)
#             k -= 1
#
#     def rotate_one(self, nums):
#         if len(nums) == 1:
#             return
#
#         temp = nums[0]
#         for idx in range(len(nums) - 1, -1, -1):
#             if idx == 0:
#                 nums[1] = temp
#             elif idx == len(nums) - 1:
#                 nums[0] = nums[idx]
#             else:
#                 nums[idx + 1] = nums[idx]
#
#
# nums = [1, 2, 3]
# k = 1
# Solution().rotate(nums, k)
# print(nums)
# nums = [1, 2, 3]
# k = 0
# Solution().rotate(nums, k)
# print(nums)
# nums = [1, 2, 3]
# k = 3
# Solution().rotate(nums, k)
# print(nums)
# nums = [1]
# k = 3
# Solution().rotate(nums, k)
# print(nums)
# nums = [1, 2]
# k = 3
# Solution().rotate(nums, k)
# print(nums)
