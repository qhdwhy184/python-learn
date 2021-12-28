class Solution:
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

# print(Solution().isPalindrome(""))
# print(Solution().isPalindrome(" "))
# print(Solution().isPalindrome("1"))
# print(Solution().isPalindrome("121"))
# print(Solution().isPalindrome("1212"))
# print(Solution().isPalindrome(",121,"))
# print(Solution().isPalindrome(",121"))
# print(Solution().isPalindrome("121, "))
# print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
print(Solution().isPalindrome(",."))
