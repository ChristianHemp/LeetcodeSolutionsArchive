# Problem: https://leetcode.com/problems/reorder-list/
# Approach: Find middle of list using fast and slow pointers. Split list in half. Reverse second half. Merge first half with newly reversed second half.
# Complexity: O(n) time, O(1) space
# Enjoyment: 2/5

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        right = head
        mid = head

        while right.next and right.next.next:
            right = right.next.next
            mid = mid.next
        
        second = mid.next
        mid.next = None

        prev = None
        curr = second
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # reversed head at prev
        while prev:
            temp = head.next
            temp2 = prev.next

            head.next = prev
            prev.next = temp

            head = temp
            prev = temp2
