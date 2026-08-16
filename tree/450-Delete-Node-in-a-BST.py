# Problem: https://leetcode.com/problems/delete-node-in-a-bst/
# Approach: 2 cases: 0-1 children return non-null, 2 children, find min val in right subtree with helper and replace curr node value, then remove min node from right subtree
# Complexity: O(log n) if tree balanced, O(n) worst case. O(1) space

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minVal = self.getMinVal(root.right)
                root.val = minVal
                root.right = self.deleteNode(root.right, minVal)
        
        return root
    
    def getMinVal(self, root):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr.val
        
