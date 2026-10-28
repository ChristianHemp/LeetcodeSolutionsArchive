# Problem: https://leetcode.com/problems/jewels-and-stones/
# Approach: Maintain set of all jewel characters, iterate through stones to find matching jewel characters
# Complexity: O(n) time, O(n) space
# Enjoyment: 3/5

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set()
        num_of_jewels = 0

        for char in jewels:
            jewel_set.add(char)
        
        for char in stones:
            if char in jewel_set:
                num_of_jewels += 1
        
        return num_of_jewels
