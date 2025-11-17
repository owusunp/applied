"""
LeetCode #110 - Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than 1.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true

Constraints:
- The number of nodes in the tree is in the range [0, 5000].
- -10^4 <= Node.val <= 10^4

THOUGHT PROCESS FOR INTERVIEWER:

**Approach**: Use bottom-up approach to check height difference at each node.

**How it works**:
- For each node, calculate height of left and right subtrees
- Check if height difference is more than 1
- If any node is unbalanced, return -1 (invalid height)
- If both subtrees are balanced, return max height + 1

**Key Points**:
- Use -1 to indicate unbalanced subtree (invalid)
- Return actual height for balanced subtrees
- Check height difference at each node
- Early termination if any subtree is unbalanced

**Example**: root = [3,9,20,null,null,15,7]
- Node 9: height = 0 (leaf)
- Node 15: height = 0 (leaf)  
- Node 7: height = 0 (leaf)
- Node 20: height = max(0,0) + 1 = 1
- Node 3: height = max(0,1) + 1 = 2
- Check: |0-1| = 1 ≤ 1 ✓

**Time Complexity**: O(n) - visit each node once.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """
        Check if binary tree is height-balanced using bottom-up approach.
        
        Args:
            root: Root of the binary tree
            
        Returns:
            True if balanced, False otherwise
        """
        # Helper function to calculate height and check balance - validate each subtree
        def getHeight(node):
            # Base case: empty node has height 0 - null nodes don't contribute to height
            if not node:
                return 0
            
            # Get height of left subtree - check if left subtree is balanced
            left_height = getHeight(node.left)
            # If left subtree is unbalanced, propagate the imbalance - early termination
            if left_height == -1:
                return -1
            
            # Get height of right subtree - check if right subtree is balanced
            right_height = getHeight(node.right)
            # If right subtree is unbalanced, propagate the imbalance - early termination
            if right_height == -1:
                return -1
            
            # Check if current node is balanced - height difference must be ≤ 1
            if abs(left_height - right_height) > 1:
                return -1  # Unbalanced - return invalid height
            
            # Return height of current node - max height of subtrees + 1 for current node
            return max(left_height, right_height) + 1
        
        # Check if tree is balanced - -1 means unbalanced, any other value means balanced
        return getHeight(root) != -1
