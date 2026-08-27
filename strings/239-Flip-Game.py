# Problem: https://leetcode.com/problems/flip-game/
# Approach: Iterate through string checking for consecutive ++, add a new string with -- inserted to list of results.
# Complexity: O(n^2) time, O(n) space
# Enjoyment: 1/5 (wording trash)

class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        res = []

        for i in range(len(currentState) - 1):
            if currentState[i] == '+' and currentState[i + 1] == '+':
                new_state = currentState[:i] + "--" + currentState[i + 2:]
                res.append(new_state)
        
        return res
