import heapq
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        pq = [(matrix[i][0], i, 0) for i in range(n)]
        heapq.heapify(pq)

        ret = 0
        for i in range(k - 1):
            num, x, y = heapq.heappop(pq)
            if y != n - 1:
                heapq.heappush(pq, (matrix[x][y + 1], x, y + 1))

        return heapq.heappop(pq)[0]



# this is a wrong solution, comment it out for backup
# class Solution:
#     def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
#         n = len(matrix)
#         begin = 1
#         end = n
#         i = int((begin + end) / 2)
#         cur = i * i
#
#         r = self.findRow(n, k)
#         return self.findNum(n, r, k, matrix)
#
#     def findNum(self, n, r, k, matrix):
#         cnt = k - (r - 1) * (r - 1)
#         idx_r = 0
#         idx_c = 0
#         res = None
#         while cnt > 0 and idx_c < n and idx_r < n:
#             if matrix[r - 1][idx_c] <= matrix[idx_r][r - 1]:
#                 res = matrix[r - 1][idx_c]
#                 idx_c += 1
#             else:  # matrix[r - 1][idx_c] > matrix[idx_r][r - 1]:
#                 res = matrix[idx_r][r - 1]
#                 idx_r += 1
#             cnt -= 1
#             if cnt == 0:
#                 return res
#
#         if idx_c < n:
#             return matrix[r - 1][idx_c + cnt - 1]
#         else:
#             return matrix[idx_r + cnt - 1][r - 1]
#
#     def findRow(self, n, k):
#         begin = 1
#         end = n
#         while begin <= end:
#             i = int((begin + end) / 2)
#             if i * i >= k:
#                 if (i - 1) * (i - 1) < k:
#                     return i
#                 end = (i - 1) * (i - 1)
#             else:  # i * i < k
#                 if (i + 1) * (i + 1) >= k:
#                     return i + 1
#                 begin = (i + 1) * (i + 1)
#
#
# # print(Solution().kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))
# # print(Solution().kthSmallest([[-5]], 1))
# # print(Solution().kthSmallest([[1,2],[1,3]], 4))
# print(Solution().kthSmallest([[1,3,5],[6,7,12],[11,14,14]], 3))