# Problem: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Approach: Use hashmap to store indices of values in inorder array. Recursively traverse tree creating new right and left nodes.
# Complexity: O(n) time, O(n) space
# Enjoyment: 1/5

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Map to store the value -> index relationship for the inorder array
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # Pointer to keep track of the current root in the preorder list
        preorder_idx = 0
        
        def array_to_tree(left_in: int, right_in: int) -> Optional[TreeNode]:
            nonlocal preorder_idx
            
            # Base case: if there are no elements to construct the subtree
            if left_in > right_in:
                return None
            
            # The first element in the current preorder range is our root value
            root_val = preorder[preorder_idx]
            root = TreeNode(root_val)
            
            # Move to the next element in preorder for subsequent recursive calls
            preorder_idx += 1
            
            # Find where this root splits the inorder array
            mid_idx = inorder_map[root_val]
            
            # Build the left subtree first (important: matching preorder sequence)
            root.left = array_to_tree(left_in, mid_idx - 1)
            
            # Build the right subtree
            root.right = array_to_tree(mid_idx + 1, right_in)
            
            return root
            
        return array_to_tree(0, len(inorder) - 1)
