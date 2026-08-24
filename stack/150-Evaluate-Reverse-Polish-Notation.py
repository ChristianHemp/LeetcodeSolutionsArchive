# Problem: https://leetcode.com/problems/evaluate-reverse-polish-notation/
# Approach: Keep hashmap mapping operations to lambda taking in two parameters num1 and num2 and returning result after appropriate operation.
#           Iterate through stack appending all non-operation values to stack, when operation reached, pop last two values and call proper lambda and re-append result to stack
#           Return final value of stack which is always result of full RPN expression.
# Complexity: O(n) time, O(n) space
# Enjoyment: 5/5


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b, 
            '*': lambda a, b: a * b, 
            '/': lambda a, b: int(a / b)
            }

        for token in tokens:
            if token not in operations:
                stack.append(int(token))
                continue

            num2 = stack.pop()  # right side of operation
            num1 = stack.pop()  # left side of operation
            operation = operations[token]
            stack.append(operation(num1, num2))

        return stack.pop()
