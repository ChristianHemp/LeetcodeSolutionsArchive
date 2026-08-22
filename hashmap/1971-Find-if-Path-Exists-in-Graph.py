# Problem: https://leetcode.com/problems/find-if-path-exists-in-graph/
# Approach: Create adjacency list based on graph edges given. Use bfs to search all vertices and edges to see if path from source to destination exists
# Complexity: O(V + E) time, O(V) space
# Enjoyment: 3/5


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list = {}

        for i in range(n):
            adj_list[i] = []
        
        for src, dst in edges:
            adj_list[src].append(dst)
            adj_list[dst].append(src)
        
        # stop early if direct path exists
        if destination in adj_list[source]:
            return True
        
        q = deque()
        visited = set()
        q.append(source)
        visited.add(source)

        while q:
            for _ in range(len(q)):
                curr = q.popleft()

                if curr == destination:
                    return True
                
                for neighbor in adj_list[curr]:
                    if neighbor not in visited:
                        q.append(neighbor)
                        visited.add(neighbor)
        
        return False
