# Problem: https://leetcode.com/problems/binary-tree-level-order-traversal/
# Approach: Keep track of result list and current sublist. Maintain a queue to know which node to process next, each time node is processed, add its children (if they exist) to the end of the queue. 
#           At each level, append a copy of the sublist to result and clear it. Nested for loop to execute set size of q times to prevent influence from newly added nodes
# Complexity: O(n) time despite nested loops as each value is still processed only once, O(n) space

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        sublist = []
        q = deque()

        if root:
            q.append(root)
        
        while len(q) > 0:
            for _ in range(len(q)):
                curr = q.popleft()
                sublist.append(curr.val)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(sublist[:])
            sublist.clear()
        
        return res
            
