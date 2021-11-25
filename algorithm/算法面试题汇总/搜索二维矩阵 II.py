from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        max_row = len(matrix)
        max_col = len(matrix[0])
        row_idx = 0
        col_idx = max_col - 1

        while 0 <= row_idx < max_row and 0 <= col_idx < max_col:
            if matrix[row_idx][col_idx] == target:
                return True
            if matrix[row_idx][col_idx] > target:
                col_idx -= 1
                continue
            if matrix[row_idx][col_idx] < target:
                row_idx += 1

        return False

print(Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5))