# Problem: https://leetcode.com/problems/counting-elements/
# Approach: Use set to keep track of elements in array and check each element for element + 1 in set
# Complexity: O(n) time, O(n) space
# Enjoyment: 3/5

class Solution:
    def countElements(self, arr: List[int]) -> int:
        in_array = set(arr)

        count = 0
        for num in arr:
            if num + 1 in in_array:
                count += 1
        
        return count
