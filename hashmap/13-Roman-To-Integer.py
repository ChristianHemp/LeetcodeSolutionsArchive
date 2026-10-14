# Problem: https://leetcode.com/problems/roman-to-integer/
# Approach: Loop through string and if value of index is less than the next subtract from total (for IV cases) if not add. Dictionary contains values.
# Complexity: O(n) time, O(1) space

class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_to_value = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0
        for i in range(len(s)):
            if (i < len(s) - 1 and 
            symbol_to_value[s[i]] < symbol_to_value[s[i + 1]]):
                total -= symbol_to_value[s[i]]
            else:
                total += symbol_to_value[s[i]]
        
        return total
