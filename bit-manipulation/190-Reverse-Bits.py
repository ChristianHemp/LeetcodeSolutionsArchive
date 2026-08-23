# Problem: https://leetcode.com/problems/reverse-bits/
# Approach: For each bit in the given 32 bit unsigned integer, get its value (0/1) and use a bitwise or with the result (starting at 0) to build the proper binary representation one bit at a time.
# Complexity: O(1) time, O(1) space
# Enjoyment: 1/5

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))
        
        return res
