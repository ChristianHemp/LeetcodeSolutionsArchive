# Problem: https://leetcode.com/problems/insert-into-a-binary-search-tree/
# Approach: Implement basic recursive tree insertion method, calling until reaching a null root value, creating the new tree node and fixing pointers.
# Complexity: O(log n) if balanced or more accurately O(h) time where h is the height of the tree, O(h) space

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        elif val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        
        return root
