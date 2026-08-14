# Problem: https://leetcode.com/problems/reverse-linked-list/
# Approach: Maintain two pointers for previous node and current node. Traverse through LL setting curr.next to prev (using temporary variable to not losee curr.next's original value).
#           Return prev which will naturally be the new head due to nature of traversal
# Complexity: O(n) time, O(1) space


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev
