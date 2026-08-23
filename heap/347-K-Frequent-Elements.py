# Problem: https://leetcode.com/problems/top-k-frequent-elements/
# Approach: Use a hashmap to keep counts of values, add a tuple containing the frequency its element to a heap that sorts based on frequency. Pop from that heap k times adding the element to res.
# Complexity: O(n log n) time, O(n) space

from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        pq = []
        res = []

        for num in nums:
            counts[num] += 1
        
        for key, val in counts.items():
            heapq.heappush_max(pq, (val, key))
        
        for _ in range(k):
            res.append(heapq.heappop_max(pq)[1])
        
        return res
