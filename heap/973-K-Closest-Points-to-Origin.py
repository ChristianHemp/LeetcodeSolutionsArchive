# Problem: https://leetcode.com/problems/k-closest-points-to-origin/
# Approach: Used merge sort algorithm that utilized euclidiean distance formula to sort coordinate pair list, then returned the first k elements in the list.
# Complexity: O(n log n) time where n is number of elements in points, O(n) space

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []

        for point in points:
            distance = math.sqrt(point[0] ** 2 + point[1] ** 2)
            heapq.heappush(minHeap, [distance, point])
        
        for _ in range(k):
            res.append(heapq.heappop(minHeap)[1])
        
        return res
