# Problem: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# Approach: recursively build tree always using mid values of the left and right subarrays
# Complexity: O(n) time, O(log n) space
# Enjoyment: 3/5

class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:

        def build(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2
            new_node = TreeNode(nums[mid])
            new_node.left = build(left, mid - 1)
            new_node.right = build(mid + 1, right)

            return new_node
        
        return build(0, len(nums) - 1)
