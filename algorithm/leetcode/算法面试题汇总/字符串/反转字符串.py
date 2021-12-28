from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        begin_idx = 0
        end_idx = len(s) - 1
        while begin_idx < end_idx:
            tmp = s[end_idx]
            s[end_idx] = s[begin_idx]
            s[begin_idx] = tmp
            begin_idx += 1
            end_idx -= 1


s = ["123321"]
Solution().reverseString(s)
print(s)

s = ["1", "2", "3", "4", "5"]
Solution().reverseString(s)
print(s)

s = []
Solution().reverseString(s)
print(s)

s = ["1", "2"]
Solution().reverseString(s)
print(s)


