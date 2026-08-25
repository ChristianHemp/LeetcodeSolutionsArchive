# Problem: https://leetcode.com/problems/daily-temperatures/
# Approach: Maintain a stack of the indices of the temperatures in descending order. Iterate through temperatures in reverse order, checking if the temperature is less than the top of the stack
#           If less, res[i] must be stack[-1] - i, append index to stack and continue iteration. If temperature[i] is larger, pop from the stack until it is less than, or the stack is empty then res[i] = difference in index or 0. Then append next index to the stack.
# Complexity: O(n) time, O(n) space
# Enjoyment: 3/5

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [len(temperatures) - 1]

        for i in range(len(temperatures) - 2, -1, -1):
            if temperatures[i] < temperatures[stack[-1]]:
                res[i] = stack[-1] - i
            else:
                while stack and temperatures[i] >= temperatures[stack[-1]]:
                    stack.pop()
                if stack:
                    res[i] = stack[-1] - i
                else:
                    res[i] = 0

            stack.append(i)

        return res
