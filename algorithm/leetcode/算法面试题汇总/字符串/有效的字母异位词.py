
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = dict()
        for _ in s:
            if _ in s_dict:
                s_dict[_] += 1
            else:
                s_dict[_] = 1

        for _ in t:
            if _ not in s_dict:
                return False
            if s_dict[_] == 0:
                return False
            s_dict[_] -= 1

        for _ in s_dict:
            if s_dict[_] != 0:
                return False

        return True


print(Solution().isAnagram("123", "321"))
print(Solution().isAnagram("1", "1"))
print(Solution().isAnagram("", ""))
print(Solution().isAnagram("", "1"))
print(Solution().isAnagram("1", ""))
print(Solution().isAnagram("12", "321"))