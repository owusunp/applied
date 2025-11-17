"""
LeetCode #98 - Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -2^31 <= Node.val <= 2^31 - 1

THOUGHT PROCESS FOR INTERVIEWER:

**Approach**: Use bounds checking to validate BST property at each node.

**How it works**:
- Each node must be within valid bounds (min_val, max_val)
- Left child must be less than parent, so max_val becomes parent's value
- Right child must be greater than parent, so min_val becomes parent's value
- Start with bounds (-infinity, +infinity) for root

**Key Points**:
- Use recursive bounds checking instead of just comparing with parent
- Left subtree: bounds are (min_val, parent.val)
- Right subtree: bounds are (parent.val, max_val)
- Return false if any node violates its bounds

**Example**: root = [5,1,4,null,null,3,6]
- Root 5: bounds (-∞, +∞) ✓
- Left 1: bounds (-∞, 5) ✓
- Right 4: bounds (5, +∞) ✗ (4 < 5, violates BST property)

**Time Complexity**: O(n) - visit each node once.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        Check if binary tree is a valid BST using bounds checking.
        
        Args:
            root: Root of the binary tree
            
        Returns:
            True if valid BST, False otherwise
        """
        # Helper function to check BST property with bounds - validate each node
        def validate(node, min_val, max_val):
            # Base case: empty node is valid - null nodes don't violate BST property
            if not node:
                return True
            
            # Check if current node violates bounds - node must be within valid range
            if node.val <= min_val or node.val >= max_val:
                return False
            
            # Recursively check left and right subtrees with updated bounds - validate subtrees
            # Left subtree: all values must be less than current node - update max bound
            # Right subtree: all values must be greater than current node - update min bound
            return (validate(node.left, min_val, node.val) and 
                    validate(node.right, node.val, max_val))
        
        # Start with bounds (-infinity, +infinity) for root - no initial restrictions
        # Use float('inf') because node values can be up to 2^31 - 1
        return validate(root, float('-inf'), float('inf'))




