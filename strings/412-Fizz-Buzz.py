# Problem: https://leetcode.com/problems/fizz-buzz/description/
# Approach: Start at 1 and go to n, check divisibility rules at each step.
# Complexity: O(n) time, O(n) space
# Enjoyment: FizzBuzz/5

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        i = 1
        while i <= n:
            if i % 3 == 0 and i % 5 == 0:
                res.append("FizzBuzz")
            elif i % 3 == 0:
                res.append("Fizz")
            elif i % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i))
            i += 1
        
        return res
        
