# Problem: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Approach: Traverse given tree in order, appending values into an array in non-descending order. Return value at index k - 1 (since 1 indexed)
# Complexity: O(n) time, O(n) space

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []

        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            values.append(root.val)
            inorder(root.right)

        inorder(root)
        return values[k - 1]
