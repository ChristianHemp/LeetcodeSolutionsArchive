# Problem: https://leetcode.com/problems/reorder-list/
# Approach: Find middle index, reverse second half of linked list from middle index, alternate between both lists and merge
# Complexity: O(n) time, O(1) space
# Enjoyment: 3/5

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        mid = head
        right = head

        # find middle index
        while right.next and right.next.next:
            mid = mid.next
            right = right.next.next
        
        temp = mid.next
        mid.next = None
        second = temp
        prev = None

        # reverse second half of linked list
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # alternate and merge both lists
        while prev:
            temp = head.next
            temp2 = prev.next

            head.next = prev
            prev.next = temp
            
            head = temp
            prev = temp2
