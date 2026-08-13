# Problem: https://leetcode.com/problems/min-stack/submissions/
# Approach: Keep track of two stacks (as arrays), one for ordinary stack application and the other to keep track of the minimum value at that level of the stack. 
#           Only update minStack when pushing value less than current minimum, which will always be at the top of minStack
# Complexity: O(1) time for all methods, O(n) space

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if self.minStack:
            value = min(value, self.minStack[-1])
            self.minStack.append(value)
        else:
            self.minStack.append(value)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
