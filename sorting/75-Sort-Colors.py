# Problem: https://leetcode.com/problems/sort-colors/
# Approach: Use bucket sort to keep track of the counts of each color, then iterate through and build back
# Complexity: O(n) time despite nested loop since still only n max possible repititions, O(1) space

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        buckets = [0, 0, 0]

        for i in nums:
            buckets[i] += 1
        
        i = 0
        for j in range(len(buckets)):
            for k in range(buckets[j]):
                nums[i] = j
                i += 1
