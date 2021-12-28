from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 0:
            return [[]]
        if len(s) == 1:
            return [[s]]

        res = []

        for idx in range(1, len(s)+1):
            cur = s[0: idx]
            if not self.isPalindrome(cur):
                continue
            c_res = self.partition(s[idx:])
            for r in c_res:
                r.insert(0, cur)
                res.append(r)
        return res

    def isPalindrome(self, s: str) -> bool:
        l = len(s)
        left_idx, right_idx = 0, l-1

        while left_idx < right_idx:
            if not s[left_idx].isalpha() and not s[left_idx].isdigit():
                left_idx += 1
                continue

            if not s[right_idx].isalpha() and not s[right_idx].isdigit():
                right_idx -= 1
                continue

            if s[left_idx].upper() != s[right_idx].upper():
                return False
            left_idx += 1
            right_idx -= 1

        return True

print(Solution().partition("a"))
print(Solution().partition("aab"))
print(Solution().partition("abcde"))
print(Solution().partition("aaaaa"))
print(Solution().partition("aabaa"))
print(Solution().partition("baa"))