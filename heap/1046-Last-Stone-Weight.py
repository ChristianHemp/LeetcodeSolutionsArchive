# Problem: https://leetcode.com/problems/last-stone-weight/
# Approach: Use a max heap to efficiently pop the two largest stones, max_heap achieved through multiplying by -1 (to not rely on heapq.heapify_max)
# Complexity: O(n log n) time, O(n) space (could be O(1) if using _max which is pyth 3.14+ exclusive for in place heapify of stones)

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for stone in stones:
            max_heap.append(stone * -1)
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            stone1 = -1 * heapq.heappop(max_heap)
            stone2 = -1 * heapq.heappop(max_heap)

            if stone1 == stone2:
                continue
            elif stone1 < stone2:
                stone2 -= stone1
                heapq.heappush(max_heap, -1 * stone2)
            else:
                stone1 -= stone2
                heapq.heappush(max_heap, -1 * stone1)
        
        if max_heap:
            return -1 * max_heap.pop()
        else:
            return 0
