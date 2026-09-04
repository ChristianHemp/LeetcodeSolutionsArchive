# Problem: https://leetcode.com/problems/subtree-of-another-tree/
# Approach: Use nested dfs at each step to check if same tree as subroot. If identical found, return true up recursion chain
# Complexity: O(n * m) time where n is size of main tre and m is size of subRoot, O(n * m) space
# Enjoyment: 2/5

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def dfs(root, subRoot):
            if not root and not subRoot:
                return True
            
            if not root or not subRoot:
                return False
            
            if root.val != subRoot.val:
                return False

            return (
                dfs(root.left, subRoot.left) and
                dfs(root.right, subRoot.right)
                )

        if root.val == subRoot.val and dfs(root, subRoot):
            return True

        if dfs(root.right, subRoot) or dfs(root.left, subRoot):
            return True

        return (
            self.isSubtree(root.left, subRoot) or 
            self.isSubtree(root.right, subRoot)
            )
        
