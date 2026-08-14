# Problem: https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/
# Approach: Create a counter to visualize how many students want each sandwich type. Iterate through sandwiches checking if there is still a student that wants that sandwich, decrementing the cnt and res
# Complexity: O(1) time, O(n) space.

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        cnt = Counter(students)

        for sandwich in sandwiches:
            if cnt[sandwich] > 0:
                res -= 1
                cnt[sandwich] -= 1
            else:
                return res
        
        return res
        
