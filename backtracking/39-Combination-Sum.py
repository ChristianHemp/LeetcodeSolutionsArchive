# Problem: https://leetcode.com/problems/combination-sum/
# Approach: Decision tree that adds same value until total exceeds targets then backtracks to test other values (ie: 2 -> 2,2 -> 2,2,2 -> 2,2,2,2 > 7 -> 2,2,2,3 > 7 -> 2,2,2,5 > 7 -> ... -> 2,2,3 == 7)
# Complexity: O(n^(target/min(candidates)) time since the max recursion depth is target/smallest value of candidates, O(target/min(candidates) space

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, sublist, curr_total):
            if curr_total == target:
                res.append(sublist[:])
                return
            
            if i >= len(candidates) or curr_total > target:
                return
            
            sublist.append(candidates[i])
            dfs(i, sublist, curr_total + candidates[i])

            sublist.pop()
            dfs(i + 1, sublist, curr_total)
        
        dfs(0, [], 0)
        return res
