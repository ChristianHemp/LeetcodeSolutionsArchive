# Problem: https://leetcode.com/problems/can-place-flowers/
# Approach: Use greedy approach, pad array with extra zeros and search for 0 indices where both neighbors also 0 then swap element to 1
# Complexity: O(n) time, O(n) space
# Enjoyment: 3/5

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        arr = [0] + flowerbed + [0]

        for i in range(1, len(arr) - 1):
            if arr[i - 1] == 0 and arr[i] == 0 and arr[i + 1] == 0:
                arr[i] = 1
                n -= 1

            if n <= 0:
                return True
        
        return False
