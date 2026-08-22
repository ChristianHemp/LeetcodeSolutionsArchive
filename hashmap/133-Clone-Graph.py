# Problem: https://leetcode.com/problems/clone-graph/
# Approach: Use a hashmap mapping original nodes to cloned nodes. Run a depth first search that traverses the graph adding new vertices to hashmap and creating edges between neighbors
# Complexity: O(V + E) time, O(V) space
# Enjoyment: 2/5


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        original_to_cloned = {}

        def dfs(node):
            if node in original_to_cloned:
                return original_to_cloned[node]
            
            copy = Node(node.val)
            original_to_cloned[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            return copy
        
        if node:
            return dfs(node)
        else:
            return None
