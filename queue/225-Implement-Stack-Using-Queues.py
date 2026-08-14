# Problem: https://leetcode.com/problems/longest-common-prefix/
# Approach: Keep one deque() and let the order rotate using push and popleft until correct value is first.
# Complexity: pop, top O(n) time, push, emtpy O(1) time, O(n) space

class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        for i in range(len(self.q) - 1):
            self.push(self.q.popleft())
        
        return self.q.popleft()

    def top(self) -> int:
        for i in range(len(self.q) - 1):
            self.push(self.q.popleft())
        
        temp = self.q.popleft()
        self.push(temp)
        return temp

    def empty(self) -> bool:
        return len(self.q) == 0
