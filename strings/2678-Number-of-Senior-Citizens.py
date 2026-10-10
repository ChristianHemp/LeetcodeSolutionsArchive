# Problem: https://leetcode.com/problems/number-of-senior-citizens/
# Approach: Get substring that represents age, cast to int and see if over 60 incrementing count for each person
# Complexity: O(n) time, O(1) space
# Enjoyment: 3/5

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0

        for detail in details:
            substr = detail[-4:-2]
            if int(substr) > 60:
                count += 1
        
        return count
