# Problem: https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/
# Approach: Keep a counter of the number of repititions to break out of loop, if beginning of queues are same remove from both queues and reset reps, otherwise add the student to end of the queue and increment reps
# Complexity: O(n^2) time, O(n) space. (optimal despite n^2)

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        reps = 0

        while reps < len(students):
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                reps = 0
            else:
                students.append(students.pop(0))
                reps += 1
        
        return len(students)
