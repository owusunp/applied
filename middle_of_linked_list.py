"""
LeetCode #876: Middle of the Linked List

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

Constraints:
- The number of nodes in the list is in the range [1, 100].
- 1 <= Node.val <= 100

THOUGHT PROCESS FOR INTERVIEWER:

**Approach**: Use the "slow and fast pointer" technique (also called "tortoise and hare").

**Key Insight**: 
If one pointer moves twice as fast as another, when the fast pointer reaches the end,
the slow pointer will be at the middle.

**How it works**:
- Use two pointers: slow and fast
- Both start at head
- slow moves 1 step at a time
- fast moves 2 steps at a time
- When fast reaches the end, slow is at the middle

**Example**: [1,2,3,4,5]

Step 0:  1 → 2 → 3 → 4 → 5 → None
         ↑
       slow, fast

Step 1:  1 → 2 → 3 → 4 → 5 → None
             ↑       ↑
           slow    fast

Step 2:  1 → 2 → 3 → 4 → 5 → None
                 ↑           ↑
               slow        fast

fast is at None (end), so slow is at middle (3)!

**Why it works**:
- slow travels n/2 steps
- fast travels n steps (2 × n/2)
- When fast reaches end (n steps), slow is at middle (n/2)

**Time**: O(n) - one pass through list
**Space**: O(1) - only two pointers
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Find the middle node using slow and fast pointers.
        
        Args:
            head: Head of the linked list
            
        Returns:
            The middle node (or second middle if two exist)
        """
        # Initialize both pointers at head
        # slow moves 1 step at a time, fast moves 2 steps
        slow = head
        fast = head
        
        # Move pointers until fast reaches the end
        # We check fast and fast.next to avoid None errors
        # fast != None: ensures fast pointer is valid
        # fast.next != None: ensures we can move fast 2 steps
        while fast and fast.next:
            # Move slow pointer 1 step forward
            # This ensures slow is at middle when fast reaches end
            slow = slow.next
            
            # Move fast pointer 2 steps forward
            # This makes fast reach end twice as fast as slow
            fast = fast.next.next
        
        # When fast reaches end, slow is at middle
        # Return slow as the middle node
        return slow


# Helper functions for testing
def create_linked_list(values):
    """Create a linked list from a list of values"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    """Convert linked list to Python list for easy printing"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    print("=== Middle of Linked List Tests ===")
    print()
    
    # Test case 1: Odd length
    values1 = [1, 2, 3, 4, 5]
    head1 = create_linked_list(values1)
    middle1 = solution.middleNode(head1)
    result1 = linked_list_to_list(middle1)
    print(f"Test 1 (odd length):")
    print(f"Input: {values1}")
    print(f"Output: {result1}")
    print(f"Expected: [3, 4, 5]")
    print()
    
    # Test case 2: Even length
    values2 = [1, 2, 3, 4, 5, 6]
    head2 = create_linked_list(values2)
    middle2 = solution.middleNode(head2)
    result2 = linked_list_to_list(middle2)
    print(f"Test 2 (even length):")
    print(f"Input: {values2}")
    print(f"Output: {result2}")
    print(f"Expected: [4, 5, 6]")
    print()
    
    # Test case 3: Single node
    values3 = [1]
    head3 = create_linked_list(values3)
    middle3 = solution.middleNode(head3)
    result3 = linked_list_to_list(middle3)
    print(f"Test 3 (single node):")
    print(f"Input: {values3}")
    print(f"Output: {result3}")
    print(f"Expected: [1]")
    print()
    
    # Test case 4: Two nodes
    values4 = [1, 2]
    head4 = create_linked_list(values4)
    middle4 = solution.middleNode(head4)
    result4 = linked_list_to_list(middle4)
    print(f"Test 4 (two nodes):")
    print(f"Input: {values4}")
    print(f"Output: {result4}")
    print(f"Expected: [2]")
    print()
    
    # Test case 5: Seven nodes
    values5 = [1, 2, 3, 4, 5, 6, 7]
    head5 = create_linked_list(values5)
    middle5 = solution.middleNode(head5)
    result5 = linked_list_to_list(middle5)
    print(f"Test 5 (seven nodes):")
    print(f"Input: {values5}")
    print(f"Output: {result5}")
    print(f"Expected: [4, 5, 6, 7]")
    print()
