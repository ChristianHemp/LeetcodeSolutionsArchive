# Problem: https://leetcode.com/problems/merge-two-sorted-lists/
# Approach: Create new linked list with random starting node. Iterate through list 1 and 2 updating new list next pointer with lowest value at each iteration.
#           Whichever list isn't empty, the rest of list is appended to end of new list, returning full list without random starting node.
# Complexity: O(n) time, O(n) space

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_node = ListNode()
        tail = new_node

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return new_node.next
