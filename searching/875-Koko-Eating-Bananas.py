# Problem: https://leetcode.com/problems/koko-eating-bananas/
# Approach: Treat possible k values as a range and binary search through those values. Update result when a new lowest value is found until binary search has concluded.
#           Calculate number of hours by adding the rounded up result of the number of bananas in a each pile by the current k. Return smallest result.
# Complexity: O(n log m) time where n is number of elements in piles and m is max value in piles, O(1) space

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right

        while left <= right:
            k = (left + right) // 2
            hours = 0

            for pile in piles:
                hours += math.ceil(pile / k)
            
            if hours <= h:
                right = k - 1
                res = min(k, res)
            else:
