# Problem: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Approach: Use dfs to count maximum heights of left and right subtrees recursively
# Complexity: O(n) time, O(n) space (callstack)
# Enjoyment: 3/5

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, height):
            if root is None:
                return 0
            
            height_left = 1 + dfs(root.left, height)
            height_right = 1 + dfs(root.right, height)

            return max(height_left, height_right)
        
        return dfs(root, 0)
