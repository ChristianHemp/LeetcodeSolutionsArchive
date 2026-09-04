# Problem: https://leetcode.com/problems/diameter-of-binary-tree/
# Approach: Dfs with nonlocal diameter variable. Update diameter with the max of left + right paths + 2 (since -1 is returned for None). Return max of the two lengths + 1
# Complexity: O(n) time, O(n) space (callstack)
# Enjoyment: 3/5

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def dfs(root):
            nonlocal diameter

            if root is None:
                return -1
            
            length_left = dfs(root.left)
            length_right = dfs(root.right)

            diameter = max(diameter, length_left + length_right + 2)

            return max(length_left, length_right) + 1
        
        dfs(root)
        return diameter
