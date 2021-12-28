from typing import List
from collections import deque


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {"+", "-", "*", "/"}
        stack = deque()
        for t in tokens:
            if t not in ops:
                stack.append(int(t))
                continue
            operand_right = stack.pop()
            operand_left = stack.pop()
            if t == '+':
                res = operand_left + operand_right
            elif t == '-':
                res = operand_left - operand_right
            elif t == '*':
                res = operand_left * operand_right
            else:
                # '/'
                res = int(operand_left / operand_right)
            stack.append(res)
        return stack.pop()


print(Solution().evalRPN(["2","1","+","3","*"]))
print(Solution().evalRPN(["4","13","5","/","+"]))
print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))

