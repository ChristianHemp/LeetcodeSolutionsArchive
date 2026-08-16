# Problem: https://leetcode.com/problems/binary-tree-inorder-traversal/
# Approach: Use a nested recursive function to traverse given tree, appending to global variable res to be returned. Inorder traversal dfs.
# Complexity: O(n) time, O(n)

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inorder(root):
            if not root:
                return
        
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        inorder(root)
        return res
