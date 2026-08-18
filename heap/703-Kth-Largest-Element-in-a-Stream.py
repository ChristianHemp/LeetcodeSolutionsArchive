# Problem: https://leetcode.com/problems/kth-largest-element-in-a-stream/
# Approach: Maintain a min heap of length k, kth largest value will always be the smallest value in the heap (hence using minheap for O(1))
# Complexity: O(n log k) time where n is number of calls to add and k is size of heap (given parameter), O(k) space

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
