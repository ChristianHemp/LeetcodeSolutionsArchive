# Problem: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
# Approach: Simulate inorder traversal to build tree from ground up. build left subtree recursively then place current node, then build right subtree recursively, placing nodes in order.
# Complexity: O(n) time, O(log n) space (callstack)
# Enjoyment: 4/5

class Solution:
    def sortedListToBST(self, head: ListNode | None) -> TreeNode | None:
        size = self.getSize(head)

        def inorder(left: int, right: int) -> TreeNode:
            nonlocal head

            # base case
            if left > right:
                return None
            
            mid = (left + right) // 2

            left = inorder(left, mid - 1)

            new_node = TreeNode(head.val)
            new_node.left = left
            
            head = head.next

            new_node.right = inorder(mid + 1, right)
            return new_node
        
        return inorder(0, size - 1)
    
    # traverses linked list and returns size of linked list
    def getSize(self, head: ListNode) -> int:
        count = 0

        while head:
            head = head.next
            count += 1

        return count
