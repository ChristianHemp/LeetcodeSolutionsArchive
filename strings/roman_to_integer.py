# Problem: https://leetcode.com/problems/roman-to-integer/
# Approach: Loop through string and if value of index is less than the next subtract from total (for IV cases) if not add. Dictionary contains values.
# Complexity: O(n) time, O(1) space

class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
            }
        total = 0
        for i in range(len(s) - 1):
            if values[s[i]] < values[s[i + 1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]
        total += values[s[-1]]
        return total
