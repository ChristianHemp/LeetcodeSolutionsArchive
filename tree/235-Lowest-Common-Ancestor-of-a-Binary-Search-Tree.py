# Problem: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Approach: Traverse down tree based on whether p and q are both less than/greater than the ancestor value. If not both same, we found divergence point thus return.
# Complexity: O(h) time, O(h) space (callstack) where h is the height of the tree
# Enjoyment: 3/5

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
