# Problem: https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/
# Approach: Cast n from int to string to make iterable, then iterate through all digits calculating digit sum and product, then % n by their sum, res of 0 means divisible
# Complexity: O(d) time, O(d) space where d is number of digits in n
# Enjoyment: 3/5

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum = 0
        digit_product = 1

        # calculate digit sum and product
        for digit in str(n):
            digit_sum += int(digit)
            digit_product *= int(digit)
        
        if n % (digit_sum + digit_product) == 0:
            return True
        return False
