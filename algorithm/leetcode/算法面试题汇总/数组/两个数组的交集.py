from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        s_nums1 = sorted(nums1)
        s_nums2 = sorted(nums2)
        idx1 = 0
        idx2 = 0
        while idx1 < len(s_nums1) and idx2 < len(s_nums2):
            if s_nums1[idx1] > s_nums2[idx2]:
                idx2 += 1
            elif s_nums1[idx1] < s_nums2[idx2]:
                idx1 += 1
            else:
                res.append(s_nums1[idx1])
                idx2 += 1
                idx1 += 1

        return res


print(Solution().intersect([1,2,3], [3,2]))
print(Solution().intersect([], [3,2]))
print(Solution().intersect([], []))
print(Solution().intersect([1], [2]))
print(Solution().intersect([1], [1]))
