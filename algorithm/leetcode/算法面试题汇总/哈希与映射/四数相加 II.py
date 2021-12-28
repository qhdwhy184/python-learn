# class Solution(object):
#     def fourSumCount(self, nums1, nums2, nums3, nums4):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :type nums3: List[int]
#         :type nums4: List[int]
#         :rtype: int
#         """
#         res = 0
#         l = len(nums1)
#         for idx1 in range(l):
#             for idx2 in range(l):
#                 for idx3 in range(l):
#                     for idx4 in range(l):
#                         if nums1[idx1] + nums2[idx2] + nums3[idx3] + nums4[idx4] == 0:
#                             res += 1
#         return res

class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        res = 0
        l = len(nums1)
        store_12 = {}
        store_34 = {}
        for idx1 in range(l):
            for idx2 in range(l):
                sum = nums1[idx1] + nums2[idx2]
                if sum in store_12:
                    store_12[sum] += 1
                else:
                    store_12[sum] = 1

        for idx3 in range(l):
            for idx4 in range(l):
                sum = nums3[idx3] + nums4[idx4]
                if -sum in store_34:
                    store_34[-sum] += 1
                else:
                    store_34[-sum] = 1
        for item in store_12:
            if item in store_34:
                res += (store_12[item] * store_34[item])
        return res

# nums1 = [1,2]
# nums2 = [-2,-1]
# nums3 = [-1,2]
# nums4 = [0,2]
#
# print(Solution().fourSumCount(nums1, nums2, nums3, nums4))