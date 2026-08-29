# Problem: https://leetcode.com/problems/time-based-key-value-store/
# Approach: Use hashmap from key to list of tuples. Tuples contain value and timestamp, get uses binary search to quickly find correct timestamp if exists.
# Complexity: O(1) set, O(log n) get, O(n) space
# Enjoyment: 4/5

from collections import defaultdict

class TimeMap:
    def __init__(self):
        self.hash_map = defaultdict(list[tuple])

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if len(self.hash_map[key]) == 0:
            return ""
        
        left, right = 0, len(self.hash_map[key]) - 1

        while left <= right:
            mid = (left + right) // 2

            if self.hash_map[key][mid][0] == timestamp:
                return self.hash_map[key][mid][1]
            elif self.hash_map[key][mid][0] < timestamp:
                left = mid + 1
            else:
                right = mid - 1
        
        if right >= 0:
            return self.hash_map[key][right][1]
        else:
            return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
