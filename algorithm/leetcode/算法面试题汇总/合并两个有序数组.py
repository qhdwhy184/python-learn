from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m_idx = m - 1
        n_idx = n - 1
        res_len = len(nums1)

        for idx in range(res_len-1, -1, -1):
            if m_idx < 0 and n_idx < 0:
                break

            if n_idx < 0 or m_idx >= 0 and nums1[m_idx] >= nums2[n_idx]:
                nums1[idx] = nums1[m_idx]
                m_idx -= 1
                continue

            if m_idx < 0 or n_idx >= 0 and nums1[m_idx] < nums2[n_idx]:
                nums1[idx] = nums2[n_idx]
                n_idx -= 1


class Solution2:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx1 = m - 1
        idx2 = n - 1
        idxR = m + n - 1
        while idx1 >= 0 and idx2 >= 0 and idxR >= 0:
            if nums1[idx1] >= nums2[idx2]:
                nums1[idxR] = nums1[idx1]
                idx1 -= 1
            else:
                nums1[idxR] = nums2[idx2]
                idx2 -= 1
            idxR -= 1

        if idx2 < 0 or idxR < 0:
            return

        if idx1 < 0:
            while idxR >= 0:
                nums1[idxR] = nums2[idx2]
                idxR -= 1
                idx2 -= 1


nums1 = [2,0]
m = 1
nums2 = [1]
n = 1
Solution().merge(nums1, m, nums2, n)
print(nums1)