# Problem: https://leetcode.com/problems/number-of-1-bits/
# Approach: While the n value is greater than 0 (since unsigned), use a bitwise and to 1, and increment count if its equal to 1. Then shift the bits to the right one place
# Complexity: O(log n) time, O(1) space

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n > 0:
            if n & 1 == 1:
                count += 1
            
            n = n >> 1
        
        return count
