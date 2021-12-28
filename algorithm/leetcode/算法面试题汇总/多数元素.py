from typing import List

class Solution4:
    def majorityElement(self, nums: List[int]) -> int:
        res = None
        count = 0
        for n in nums:
            if res is None:
                res = n
                count = 1
            elif res == n:
                count += 1
            elif count > 1:
                count -= 1
            else:
                res = n

        return res


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        return self._majorityElement(nums, False)

    def _majorityElement(self, nums: List[int], all_positive) -> int:
        locs = list()
        total = len(nums)
        for i in range(0, 32):
            count = 0
            for num in nums:
                if (num >> i & 1) == 1:
                    count += 1
            # locs[i] = 1 if count > total / 2 else 0
            locs.append(1 if count > total / 2 else 0)

        res = 0

        last = 32 if all_positive else 31
        for i in range(0,last):
            res += ((2**i) * (locs[i]))

        if not all_positive and locs[31] == 1:
            for i in range(0, len(nums)):
                nums[i] = nums[i] * -1
            return self._majorityElement(nums, True) * -1

        return res


class Solution2(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = dict()
        for n in nums:
            if n in d:
                d[n] = d[n] + 1
            else:
                d[n] = 1
        for k in d:
            if d[k] > len(nums)/2:
                return k

class Solution3(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums = self.qsort(nums)
        print(nums)
        import math
        return nums[math.floor(len(nums)/2)]

    def qsort(self, nums):
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return nums
        l = 0
        h = len(nums) - 1
        pivot = nums[l]
        while l < h:
            while l < h and pivot <= nums[h]:
                h -= 1
            if l < h:
                nums[l] = nums[h]
                l += 1
            while l < h and pivot >= nums[l]:
                l += 1
            if l < h:
                nums[h] = nums[l]
                h -= 1
        nums[l] = pivot
        return self.qsort(nums[:l])+[pivot]+self.qsort(nums[l+1:])

        # return nums

print(Solution4().majorityElement([3,2,3]))
print(Solution4().majorityElement([1]))
print(Solution4().majorityElement([1,65535,1]))
print(Solution4().majorityElement([1,65535,1,3,4,1,65535,65535,65535,65535,65535,4,65535,65535]))
print(Solution4().majorityElement([-2147483648]))
# print(int(3/2))
# import math
# print(math.floor(3/2))