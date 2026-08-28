# Problem: https://leetcode.com/problems/linked-list-cycle/
# Approach: Use two pointers, one that moves 2 nodes at a time one that moves 1 node at a time. With no cycles, the fast node will reach end and return False, if it ever becomes equal to slow, return True.
# Complexity: O(n) time, O(1) space
# Enjoyment: 3/5

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        
        fast = head.next
        slow = head

        while slow != fast:
            if fast is None or fast.next is None:
                return False
            fast = fast.next.next
            slow = slow.next

        return True


