# Problem: https://leetcode.com/problems/reverse-nodes-in-k-group/
# Approach: Reverse linked list in segments of size k using 3 pointers, loop until remaining segment is less than k then return
# Complexity: O(n) time, O(1) space
# Enjoyment: 5/5 (milestone: first hard problem full blind no help)

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        final_head = None
        
        curr = start = head
        residual = None
        while curr:
            for _ in range(k - 1):
                curr = curr.next
                if curr is None:
                    break

            if curr is None:
                break
            
            # relinks last segment tail with new segment head
            if residual:
                residual.next = curr

            if final_head is None:
                final_head = curr

            next_node = curr.next
            prev = next_node
            residual = start
            # reverse linked list segment, maintain segment head pointer (residual)
            while start != next_node:
                temp = start.next
                start.next = prev
                prev = start
                start = temp
            
            curr = next_node

        return final_head if final_head is not None else head
