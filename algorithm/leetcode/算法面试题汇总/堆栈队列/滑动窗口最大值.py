import heapq
from typing import List


class Item:
    def __init__(self, val, index):
        self.val = val
        self.index = index

    def __lt__(self, other):
        return self.val >= other.val


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = []

        for idx in range(0, k):
            heapq.heappush(max_heap, Item(nums[idx], idx))

        res = []
        item = max_heap[0]
        res.append(item.val)

        for start_idx in range(1, len(nums) - k + 1):
            heapq.heappush(max_heap, Item(nums[start_idx + k - 1], start_idx + k - 1))
            item = max_heap[0]
            while item.index < start_idx:
                heapq.heappop(max_heap)
                item = max_heap[0]
            res.append(item.val)
        return res


# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         res = []
#         for start_idx in range(0, len(nums) - k + 1):
#             max_val = None
#             for idx in range(start_idx, start_idx + k):
#                 if max_val is None or max_val < nums[idx]:
#                     max_val = nums[idx]
#             res.append(max_val)
#         return res



# print(Solution().maxSlidingWindow([1, 3, 5, 6, 7, 12, 1, 14, 14], 3))
print(Solution().maxSlidingWindow([1,-9,8,-6,6,4,0,5], 4))
