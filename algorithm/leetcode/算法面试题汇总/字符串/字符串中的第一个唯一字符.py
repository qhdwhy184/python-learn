from collections import OrderedDict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        tmp = OrderedDict()
        for idx in range(0, len(s)):
            if s[idx] not in tmp:
                tmp[s[idx]] = [idx, 1]
                continue
            tmp[s[idx]][1] += 1

        for _ in tmp:
            if tmp[_][1] == 1:
                return tmp[_][0]
        return -1


print(Solution().firstUniqChar("123321"))
print(Solution().firstUniqChar("0123321"))
print(Solution().firstUniqChar("1230321"))
print(Solution().firstUniqChar("12303210"))
print(Solution().firstUniqChar("0"))
print(Solution().firstUniqChar(""))
print(Solution().firstUniqChar("00"))
print(Solution().firstUniqChar("000"))
