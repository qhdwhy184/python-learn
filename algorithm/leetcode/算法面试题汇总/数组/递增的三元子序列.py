from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min_first = None
        for first_idx in range(len(nums)):
            first = nums[first_idx]

            if min_first is None:
                min_first = first
            elif min_first <= first:
                continue
            else:
                min_first = first

            min_second = None
            for second_idx in range(first_idx + 1, len(nums)):
                second = nums[second_idx]

                if first >= second:
                    continue

                if min_second is None:
                    min_second = second
                elif min_second <= second:
                    continue
                else:
                    min_second = second

                for third_idx in range(second_idx + 1, len(nums)):
                    third = nums[third_idx]
                    if second >= third:
                        continue
                    else:
                        return True
        return False


print(Solution().increasingTriplet(nums = [1,0,0,10,0,0,100]))
print(Solution().increasingTriplet(nums = [2,1,5,0,4,6]))
print(Solution().increasingTriplet(nums = [1,2,3,4,5]))
print(Solution().increasingTriplet(nums = [5,4,3,2,1]))
print(Solution().increasingTriplet(nums = [2,1]))
print(Solution().increasingTriplet(nums = [1]))
print(Solution().increasingTriplet(nums = [1,2,3]))