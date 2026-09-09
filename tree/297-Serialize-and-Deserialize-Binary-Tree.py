# Problem: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# Approach: Use dfs for both functions (preorder). 1st serializes values using delimiter % and null to represent empty nodes. 2nd keeps track of list of nodes in preorder, building back tree accordingly
# Complexity: O(n) time, O(n) space
# Enjoyment: 4/5

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        strs = []

        def dfs(node):
            if node is None:
                strs.append("null")
                return

            strs.append(str(node.val))

            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return '%'.join(strs)
            
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        strs = data.split('%')
        index = 0

        def dfs():
            nonlocal index

            if strs[index] == 'null':
                index += 1
                return None
            
            node = TreeNode(int(strs[index]))
            index += 1

            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()
