# Problem: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Approach: Use two pointers, traverse one pointer n+1 times so gap is size n. Traverse both pointers while front pointer not None. Second pointer will be one before removal index.
# Complexity: O(n) time, O(1) space
# Enjoyment: 4/5

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head

        first = dummy
        second = dummy

        # traverse first pointer n+1 times so gap between first and second is n
        for i in range(n + 1):
            first = first.next
        
        # traverse both pointers still first is None
        while first:
            first = first.next
            second = second.next
        
        # second pointer will be at 1 before removal index
        second.next = second.next.next
        return dummy.next
