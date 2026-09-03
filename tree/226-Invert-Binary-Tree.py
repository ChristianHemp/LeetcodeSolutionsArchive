# Problem: https://leetcode.com/problems/invert-binary-tree/
# Approach: swap nodes left and right pointers pointing at, recursively invert left and right subtrees
# Complexity: O(n) time, O(n) space (callstack)
# Enjoyment: 3/5

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
