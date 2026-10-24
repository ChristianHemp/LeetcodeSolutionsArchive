# Problem: https://leetcode.com/problems/reverse-bits/
# Approach: Check if each bit is set, while building binary string from original bitwise representation's least significant to most significant bit, returning value of binary string
# Complexity: O(1) time, O(1) space
# Enjoyment: 4/5

class Solution:
    def reverseBits(self, n: int) -> int:
        result = []

        for i in range(32):
            if n & (1 << i):
                result.append("1")
            else:
                result.append("0")
        
        return int(''.join(result), 2)  # returns binary format of resulting string
