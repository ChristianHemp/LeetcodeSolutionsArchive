# Problem: https://leetcode.com/problems/task-scheduler/
# Approach: Use max heap to keep track of elements that cause bottlenecks/CPU idle. Calculate time based on maxheap counts
# Complexity: O(n) time, O(n) space
# Enjoyment: 3/5

from collections import defaultdict

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = defaultdict(int)

        for task in tasks:
            counts[task] += 1
        
        # largest counts ordered first since large counts can cause idle
        heap = [-val for val in counts.values()]
        heapq.heapify(heap)

        q = deque()
        time = 0

        # simulate tasks through time intervals
        while heap or q:
            time += 1

            if heap:
                count = heapq.heappop(heap) + 1

                if count < 0:
                    q.append((time + n, count))
            
            if q and q[0][0] == time:
                _, count = q.popleft()
                heapq.heappush(heap, count)
        
        return time
