# Problem: https://leetcode.com/problems/largest-unique-number/
# Approach: Maintain frequency map, look for keys with 1 frequencies and return largest
# Complexity: O(n) time, O(n) space
# Enjoyment: 3/5

from collections import defaultdict

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        frequency_map = defaultdict(int)

        for num in nums:
            frequency_map[num] += 1
        
        largest = -1

        for key, value in frequency_map.items():
            if value != 1:
                continue
            
            largest = max(largest, key)
        
        return largest
