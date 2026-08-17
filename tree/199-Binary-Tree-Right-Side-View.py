# Problem: https://leetcode.com/problems/binary-tree-right-side-view/
# Approach: Do a level order traversal, at the end of each level append the current val which will always be the final node in that level (furthest right)
# Complexity: O(n) time, O(n) space

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque()

        if root:
            q.append(root)


        while len(q) > 0:
            for _ in range(len(q)):
                curr = q.popleft()

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(curr.val)
        return res
