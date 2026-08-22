# Problem: https://leetcode.com/problems/course-schedule/
# Approach: Represent prereq map as a graph adjacency list. For each course traverse the graph using a set to keep track of potential cycles.
#           Immediately return false upon finding any cycle, otherwise if course is completable (dfs goes to node with empty prereqs list in adj list) remove from visited and clear prereqs to ensure no double visiting
# Complexity: O(n + p) time, O(n + p) space where n is num of courses and p is num of prereqs (edges)
# Enjoyment: 2/5

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {}

        for i in range(numCourses):
            prereqs[i] = []
        
        for crs1, crs2 in prerequisites:
            prereqs[crs1].append(crs2)
        
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            
            if prereqs[course] == []:
                return True
            
            visited.add(course)

            for neighbor in prereqs[course]:
                if not dfs(neighbor):
                    return False
            
            visited.remove(course)
            prereqs[course] = []

            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True

