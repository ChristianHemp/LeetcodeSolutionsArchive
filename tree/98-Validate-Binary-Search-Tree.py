# Problem: https://leetcode.com/problems/validate-binary-search-tree/
# Approach: Use dfs passing a range of valid values that check each child's validity
# Complexity: O(n) time, O(n) space (callstack)
# Enjoyment: 4/5

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
    
        valid = True

        def dfs(node, low, high):
            nonlocal valid

            if not node:
                return
            
            if not valid:
                return

            if node.val <= low or node.val >= high:
                valid = False

            dfs(node.left, low, node.val)
            dfs(node.right, node.val, high)
        
        dfs(root, float('-inf'), float('inf'))
        return valid
