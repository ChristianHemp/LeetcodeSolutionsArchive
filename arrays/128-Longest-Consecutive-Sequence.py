# Problem: https://leetcode.com/problems/longest-consecutive-sequence/
# Approach: Use a set to avoid duplicates, iterate through the set if the number could be the start of a sequence (num - 1 not in the set), start adding to length until the number + length isnt in the set anymore. longest is the max of prev longest and curr length.
# Complexity: O(n) time, O(n) space
# Enjoyment: 3/5


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 in num_set:
                continue
            
            length = 1
            while num + length in num_set:
                length += 1

            longest = max(length, longest)

        return longest
