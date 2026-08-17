# Problem: https://leetcode.com/problems/path-sum/
# Approach: Use depth first search (with backtracking) to search various paths of the tree. Keep track of curr_sum which is immutable thus can be used as a tracker in each call for whether a path has been found with the correct sum
# Complexity: O(n) time, O(h) space where h is the height of the tree (call stack space)

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def hasPathSumHelper(root, curr_sum):
            if not root:
                return False
            
            curr_sum += root.val

            if not root.left and not root.right:
                return curr_sum == targetSum
            if hasPathSumHelper(root.left, curr_sum):
                return True
            if hasPathSumHelper(root.right, curr_sum):
                return True

            return False
        
        return hasPathSumHelper(root, 0)
