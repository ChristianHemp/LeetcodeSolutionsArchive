# Problem: https://leetcode.com/problems/guess-number-higher-or-lower/
# Approach: Slightly modified binary search, instead of array indices use guess api to decide where to shift bounds
# Complexity: O(log n) time, O(1) space

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n

        while left <= right:
            mid = (left + right) // 2

            if guess(mid) == 1:
                left = mid + 1
            elif guess(mid) == -1:
                right = mid - 1
            else:
                return mid
