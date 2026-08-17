# Problem: https://leetcode.com/problems/balanced-binary-tree/
# Approach: used a recursive dfs to calculate heights postorder, returns height of subtree using -1 as a flag for finding an imbalance.
# Complexity: O(n) time, O(1) space

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            # handles previously found imbalances
            if left == -1 or right == -1:
                return -1

            if abs(left - right) > 1:
                return -1 # -1 value flags imbalance
            
            return 1 + max(left, right)

        return dfs(root) != -1
