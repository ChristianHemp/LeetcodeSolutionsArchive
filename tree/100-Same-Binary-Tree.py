# Problem: https://leetcode.com/problems/same-tree/
# Approach: Simultaneously run dfs on both trees checking if equal at each step
# Complexity: O(n) time, O(n) space (callstack)
# Enjoyment: 3/5

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:   
        if not p and not q:
            return True

        if not q or not p:
            return False
        
        if p.val != q.val:
            return False

        return (
            self.isSameTree(p.left, q.left) and
            self.isSameTree(p.right, q.right)
            )
