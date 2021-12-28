from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []

        if len(s) == 0:
            return None

        wordSet = set(wordDict)

        for idx in range(1, len(s) + 1):
            cur = s[0: idx]
            if cur in wordSet:
                sub_res = self.wordBreak(s[idx:], wordDict)
                if sub_res is None:
                    res.append(cur)
                    continue
                if len(sub_res) > 0:
                    for item in sub_res:
                        res.append(cur + " " + item)
        return res

print(Solution().wordBreak("aaaaa", ["aaa", "aa"]))
print(Solution().wordBreak("abc", ["a", "bc"]))
print(Solution().wordBreak("abc", ["a", "b", "c"]))
print(Solution().wordBreak("abc", ["ab", "bc"]))

    # def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
    #     res_mem = {} # idx, list[str]
    #     return self.innerWordBreak(s, wordDict, res_mem, 0)
    #
    # def innerWordBreak(self, s: str, wordDict: List[str], res_mem, start_idx) -> List[str]:
    #     # if start_idx in res_mem:
    #     #     return res_mem[start_idx]
    #
    #     l = len(s)
    #
    #     if l == start_idx:
    #         return []
    #
    #     wordSet = set(wordDict)
    #     for idx in range(start_idx + 1, l + 1):
    #         cur = s[start_idx: idx]
    #         if cur in res_mem:
    #             return res_mem[cur]
    #         if cur in wordSet:
    #              self.innerWordBreak(s, wordDict, res_mem, idx):
    #                 # No need to record True since the whole work is done when found True.
    #                 # res_mem[idx] = True
    #                 return True
    #             res_mem[idx] = False
    #
    #     return False
