# Problem: https://leetcode.com/problems/number-of-1-bits/
# Approach: Check all 32 bits to see if they are set, incrementing count when a set bit is found
# Complexity: O(1) time, O(1) space
# Enjoyment: 3/5

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        for i in range(32):
            if n & (1 << i):
                count += 1
        
        return count
