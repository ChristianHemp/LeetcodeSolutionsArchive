# Problem: https://leetcode.com/problems/linked-list-cycle/
# Approach: Keep hashmap of seen nodes and cycle through linkedlist looking for dupliactes
# Complexity: O(n) time, O(n) space

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        
        while head != None:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        
        return False
