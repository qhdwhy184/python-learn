from typing import List, Dict


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        res_mem = {}
        return self.innerWordBreak(s, wordDict, res_mem, 0)

    def innerWordBreak(self, s: str, wordDict: List[str], res_mem, start_idx) -> bool:
        if start_idx in res_mem:
            return res_mem[start_idx]

        l = len(s)

        if l == start_idx:
            return True

        wordSet = set(wordDict)
        for idx in range(start_idx + 1, l + 1):
            cur = s[start_idx: idx]
            if cur in res_mem:
                return res_mem[cur]
            if cur in wordSet:
                if self.innerWordBreak(s, wordDict, res_mem, idx):
                    # No need to record True since the whole work is done when found True.
                    # res_mem[idx] = True
                    return True
                res_mem[idx] = False

        return False


print(Solution().wordBreak("aaaaa", ["aaa", "aa"]))
print(Solution().wordBreak("abc", ["a","bc"]))
print(Solution().wordBreak("abc", ["a","b","c"]))
print(Solution().wordBreak("abc", ["ab","bc"]))
import datetime
print("start:{}".format(datetime.datetime.now()))
print(Solution().wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
print("end:{}".format(datetime.datetime.now()))

