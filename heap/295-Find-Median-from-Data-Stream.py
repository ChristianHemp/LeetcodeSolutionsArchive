# Problem: https://leetcode.com/problems/find-median-from-data-stream/
# Approach: Maintain two heaps one with smaller half (maxheap) of values form data stream and the other with larger half (minheap). Median will always be the first element of either heap or the average of the two.
# Complexity: O(log n) addNum, O(1) find Median, O(n) space
# Enjoyment: 4/5

class MedianFinder:
    def __init__(self):
        self.small = []  # smaller-values half heap
        self.large = []  # larger-values half heap

    def addNum(self, num: int) -> None:
        # add value to correct heap
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)
        
        # rebalance if necessary
        if len(self.small) > len(self.large) + 1:
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, -val)
        elif len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        elif len(self.small) < len(self.large):
            return float(self.large[0])
        else:
            return (-self.small[0] + self.large[0]) / 2
