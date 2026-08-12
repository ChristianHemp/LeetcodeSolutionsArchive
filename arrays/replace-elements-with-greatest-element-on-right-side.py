# Problem: https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
# Approach: Traverse from right to left to preserve O(n) time, keep track of largest value on the right while traversing array updating arr[i] the current max_right at each index, updating max_right value if necessary
# Complexity: O(n) time, O(1) space

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_right = -1

        for i in range(len(arr) - 1, -1, -1):
            curr = arr[i]
            arr[i] = max_right
            max_right = max(max_right, curr)
        
        return arr
