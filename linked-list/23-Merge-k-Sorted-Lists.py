# Problem: https://leetcode.com/problems/merge-k-sorted-lists/
# Approach: Used merge logic from LC 21, takes two sorted lists and merges them into one sorted list. Check if lists is empty, and return none.
#           While the length of lists is greater than 1, keep a temporary list of combined lists and iterate with jumps of 2 across lists combining lists at indices i and i + 1
#           If odd number, handles by appending the final list to temp list. Lists is updated with temp list and loop continues until 1 lists remains. Return first element of final list.
# Complexity: O(n log k) time where n is number of elements in each list and k is number of lists, O(n) space

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Example Logic:
        # Merge lists 1 and 2   Combine 1 and 2   Combine 1-2 and 3-4
        # Merge lists 3 and 4
        # Merge lists 5 and 6   Combine 3 and 4
        # Merge lists 7 and 8

        if not lists:
            return None

        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                if i + 1 < len(lists):
                    newList = self.mergeTwoLists(lists[i], lists[i + 1])
                    merged_lists.append(newList)
                else:
                    merged_lists.append(lists[i])
            lists = merged_lists

        return lists[0]
                    
    
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
        
