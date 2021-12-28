from collections import deque


class Solution:
    def calculate(self, s: str) -> int:
        stack = deque()
        cur_num = None
        pre_op = None
        for idx in range(len(s)):
            last_idx = False
            if idx == len(s) - 1:
                last_idx = True

            # not last idx
            ch = s[idx]
            if ch == ' ':
                if not last_idx:
                    continue

            if ch.isdigit():
                if cur_num is None:
                    cur_num = ch
                else:
                    cur_num += ch
                if not last_idx:
                    continue

            if pre_op is None:
                stack.append(int(cur_num))
            elif pre_op == '+':
                stack.append(int(cur_num))
            elif pre_op == '-':
                stack.append(int(cur_num) * -1)
            elif pre_op == '*':
                pre_num = stack.pop()
                tmp = int(cur_num) * pre_num
                stack.append(tmp)
            elif pre_op == '/':
                pre_num = stack.pop()
                tmp = int(pre_num / int(cur_num))
                stack.append(tmp)
            pre_op = ch
            cur_num = None

        res = 0
        for item in stack:
            res += item
        return res



print(Solution().calculate("3+2*2"))
print(Solution().calculate(" 3/2 "))
print(Solution().calculate(" 3+5 / 2 "))

