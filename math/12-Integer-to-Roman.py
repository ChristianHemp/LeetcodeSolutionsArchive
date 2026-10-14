# Problem: https://leetcode.com/problems/integer-to-roman/
# Approach: Use list of all possible symbols with cooresponding value as tuples, greedy to always pick largest possible digit representation at each step, multiplying by count and continuing with remainder using divmod
# Complexity: O(1) time, O(1) space
# Enjoyment: 3/5

class Solution:
    def intToRoman(self, num: int) -> str:
        digits = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]
        

        symbols = []
        remaining = num
        for value, symbol in digits:
            if remaining == 0:
                break
            
            count, remaining = divmod(remaining, value)

            symbols.append(symbol * count)
        
        return ''.join(symbols)
