import math


class Solution:
    def superEggDrop(self, k: int, n: int) -> int:

        # if k is large enough
        res = math.floor(math.log2(n)) + 1
        min_k = math.floor(math.log2(n + 1))
        if min_k <= k:
            return res
        egg_cnt = k
        floor_cnt = n
        while egg_cnt > 1:
            # this is incorrect here because it's not a minimum move by binary search.
            # think about the case: 100 floor, and 2 eggs, the minimum move is 20 but not 51.
            floor_cnt = math.floor((floor_cnt - 1) / 2)
            egg_cnt -= 1
        return k - 1 + floor_cnt

class Solution2:
    def superEggDrop(self, k: int, n: int) -> int:
        memo = {}
        def dp(k, n):
            if (k, n) not in memo:
                if n == 0:
                    ans = 0
                elif k == 1:
                    ans = n
                else:
                    lo, hi = 1, n
                    # keep a gap of 2 x values to manually check later
                    while lo + 1 < hi:
                        x = (lo + hi) // 2
                        t1 = dp(k - 1, x - 1)
                        t2 = dp(k, n - x)

                        if t1 < t2:
                            lo = x
                        elif t1 > t2:
                            hi = x
                        else:
                            lo = hi = x

                    ans = 1 + min(max(dp(k - 1, x - 1), dp(k, n - x))
                                  for x in (lo, hi))

                memo[k, n] = ans
            return memo[k, n]

        return dp(k, n)


# print(Solution().superEggDrop(1, 2))
# print(Solution().superEggDrop(1, 3))
# print(Solution().superEggDrop(1, 4))
# print(Solution().superEggDrop(2, 6))
# print(Solution().superEggDrop(3, 14))
# print(Solution().superEggDrop(4, 14))

print(Solution().superEggDrop(2, 9))
print(Solution2().superEggDrop(2, 9))
