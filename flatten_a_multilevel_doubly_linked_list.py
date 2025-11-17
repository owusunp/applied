"""
LeetCode #430 - Flatten a Multilevel Doubly Linked List

You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, and an additional child pointer. This child pointer may or may not point to a separate doubly linked list, also with these special pointers. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure.

Given the head of the first level of the list, flatten the list so that all the nodes appear in a single-level, doubly linked list. Let curr be a node with a child list. The nodes in the child list should appear after curr and before curr.next in the flattened list.

Return the head of the flattened list.

Example 1:
Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]

Example 2:
Input: head = [1,2,null,3]
Output: [1,3,2]

Constraints:
- The number of Nodes will not exceed 1000.
- 1 <= Node.val <= 10^5

THOUGHT PROCESS FOR INTERVIEWER:

The challenge is flattening a multilevel doubly linked list. Let me think through this:

1. **Problem Analysis**: 
   - Each node can have a child list that needs to be inserted between current and next
   - Child lists can have their own children (nested structure)
   - Need to maintain doubly linked list properties (prev/next pointers)

2. **Approach Options**:
   - **Iterative**: Use stack to handle nested children
   - **Recursive**: Natural fit for nested structure
   - **Recursive is cleaner**: Each level handled the same way

3. **Key Steps**:
   - Traverse the main list
   - When child found: recursively flatten it
   - Insert flattened child between current and current.next
   - Continue traversal

4. **Critical Details**:
   - Store current.next before flattening (will be overwritten)
   - Find tail of flattened child to reconnect with original next
   - Clear child pointer after flattening
   - Handle prev pointers correctly

**Example walkthrough**:
- List: 1-2-3-4, where 2 has child 7-8-9
- Process: 1 → 2 (has child) → flatten 7-8-9 → insert between 2 and 3
- Result: 1-2-7-8-9-3-4

This gives us O(n) time complexity where n is total nodes!
"""

class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        # Handle edge case: empty list
        if not head:
            return head
        
        # Start from the head of the list
        current = head
        
        # Traverse the list to find nodes with children
        while current:
            # If current node has a child, flatten it
            if current.child:
                # Store the next node of current - needed to reconnect after flattening
                next_node = current.next
                
                # Flatten the child list recursively - handle nested children
                child_head = self.flatten(current.child)
                
                # Connect current to the flattened child list
                current.next = child_head
                child_head.prev = current
                
                # Find the tail of the flattened child list - needed to reconnect with next_node
                tail = child_head
                while tail.next:
                    tail = tail.next
                
                # Connect the tail of child list to the original next node
                tail.next = next_node
                if next_node:
                    next_node.prev = tail
                
                # Clear the child pointer - flattening is complete
                current.child = None
            
            # Move to the next node in the list
            current = current.next
        
        # Return the head of the flattened list
        return head
