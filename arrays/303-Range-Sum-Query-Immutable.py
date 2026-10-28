# Problem: https://leetcode.com/problems/range-sum-query-immutable/
# Approach: use prefixes to get sum of all values up to i, then return right pointer prefixes minus left pointer prefixes
# Complexity: O(n) time for init, O(1) for sumRange, O(n) space
# Enjoyment: 3/5

class NumArray:

    def __init__(self, nums: list[int]):
        self.prefix = [0]

        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
