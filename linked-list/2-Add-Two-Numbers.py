# Problem: https://leetcode.com/problems/add-two-numbers/
# Approach: Loop while l1, l2, and carryover still have values (not none or 0), use modulo and floor division to get carryover/new values and append to dummy list.
# Complexity: O(n + m) time where n is len of l1 and m is len of l2, O(n + m) space
# Enjoyment: 4/5

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)

        carryover = 0
        curr = dummy
        while l1 != None or l2 != None or carryover != 0:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0

            res = num1 + num2 + carryover
            carryover = res // 10

            new_node = ListNode(res % 10)
            curr.next = new_node
            curr = new_node
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
