from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        multi_res = [None for _ in range(len(nums))]
        for idx in range(len(nums)):
            if idx == 0:
                multi_res[idx] = [1, None]
                continue
            multi_res[idx] = [nums[idx-1] * multi_res[idx-1][0], None]

        for idx in range(len(nums) - 1, -1, -1):
            if idx == len(nums) - 1:
                multi_res[idx][1] = 1
                continue
            multi_res[idx][1] = nums[idx+1] * multi_res[idx+1][1]
        res = []
        for idx in range(len(multi_res)):
            res.append(multi_res[idx][0] * multi_res[idx][1])
        return res


print(Solution().productExceptSelf([1,2,3,4]))
print(Solution().productExceptSelf([-1,1,0,-3,3]))