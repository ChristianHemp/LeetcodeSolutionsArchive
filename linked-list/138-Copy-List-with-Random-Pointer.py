# Problem: https://leetcode.com/problems/copy-list-with-random-pointer/
# Approach: Interweave new nodes into original linked lists, traverse to add random pointers, delink old nodes and return
# Complexity: O(n) time, O(1) space (except new nodes/no hashmap used)
# Enjoyment: 4/5

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # Interlink old and new nodes
        curr = head
        while curr:
            new_node = Node(curr.val, None, None)

            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next
        
        # copy random pointers
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            else:
                curr.next.random = None
            curr = curr.next.next
        
        # Keep only new nodes
        curr = head.next
        curr_old = head
        new_head = head.next

        while curr_old:
            curr_old.next = curr_old.next.next
            if curr.next:
                curr.next = curr.next.next
            else:
                curr.next = None
            curr = curr.next
            curr_old = curr_old.next
        
        return new_head
