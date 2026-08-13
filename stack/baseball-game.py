# Problem: https://leetcode.com/problems/baseball-game/
# Approach: Append digits into stack after checking for and executing specialized operations. Returns the sum of all digits in stack.
# Complexity: O(n) time, O(n) space

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == "+":
                new_num = stack[-1] + stack[-2]
                stack.append(new_num)
            elif op == "C":
                stack.pop()
            elif op == "D":
                new_num = stack[-1] * 2
                stack.append(new_num)
            else:
                stack.append(int(op))

        return sum(stack)
