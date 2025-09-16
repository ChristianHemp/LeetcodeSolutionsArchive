# Problem: https://leetcode.com/problems/plus-one/
# Approach: Convert list of digits to single string, convert string to an int and add one, check to see if new list length required (999 --> 1000) append digits (string form)
# Complexity: O(n) time, O(n) space

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = ''
        number_list = []
        for num in digits:
            number += str(num)

        number = int(number)
        number += 1

        if len(str(number)) > len(digits):
            number = str(number)
            for i in range(len(digits) + 1):
                number_list.append(number[i])
        else:
            number = str(number)
            for i in range(len(digits)):
                number_list.append(number[i])

        for i in range(len(number_list)):
            number_list[i] = int(number_list[i])

        return(number_list)
