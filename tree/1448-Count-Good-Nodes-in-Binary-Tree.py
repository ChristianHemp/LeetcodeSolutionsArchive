# Problem: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# Approach: Keep track of largest node seen in path while performing dfs, updating a nonlocal result counter
# Complexity: O(n) time, O(n) space (callstack)
# Enjoyment: 3/5

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        res = 0
        path_max = root.val

        def dfs(node, path_max):
            nonlocal res

            if node is None:
                return
            
            if node.val >= path_max:
                res += 1
                path_max = node.val

            dfs(node.left, path_max)
            dfs(node.right, path_max)

        
        dfs(root, path_max)
        return res
