"""
LeetCode #380 - Insert Delete GetRandom O(1)

Implement the RandomizedSet class:

- RandomizedSet() Initializes the RandomizedSet object.
- bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
- bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
- int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.

You must implement the functions of the class such that each function works in average O(1) time complexity.

Example 1:
Input:
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output:
[null, true, false, true, 2, true, false, 2]

Constraints:
- -2^31 <= val <= 2^31 - 1
- At most 2 * 10^5 calls will be made to insert, remove, and getRandom.
- There will be at least one element in the data structure when getRandom is called.

THOUGHT PROCESS FOR INTERVIEWER:

The challenge is achieving O(1) for all three operations. Let me think through this:

1. **HashSet approach**: 
   - Insert/Delete O(1): Hash function maps key to bucket, direct access
   - GetRandom O(n): Need to iterate through all elements to pick random one
   - Problem: Can't get random element efficiently

2. **Array approach**: 
   - GetRandom O(1): Direct access by random index
   - Delete O(n): Need to shift all elements after deleted element
   - Problem: Deletion is expensive

3. **Hybrid approach**: Use both dictionary and array
   - Dictionary: O(1) lookup for existence and index
   - Array: O(1) random access and swap operations

**Key Insight**: When deleting from array, swap the element with the last element, then remove from end.

**Example walkthrough**:
- Insert 1: values=[1], val_to_index={1:0}
- Insert 2: values=[1,2], val_to_index={1:0, 2:1}  
- Insert 3: values=[1,2,3], val_to_index={1:0, 2:1, 3:2}
- Remove 2: 
  * Find index of 2: index=1
  * Swap with last element: values=[1,3,3], val_to_index={1:0, 2:1, 3:1}
  * Update mapping: val_to_index={1:0, 3:1}
  * Remove last: values=[1,3], val_to_index={1:0, 3:1}
- GetRandom: Pick random index from [0,1] → return 1 or 3

This gives us O(1) for all operations!
"""

import random

class RandomizedSet:
    def __init__(self):
        # Dictionary to store value to index mapping - needed for O(1) lookup and removal
        self.val_to_index = {}
        # List to store all values - needed for O(1) random access
        self.values = []
    
    def insert(self, val: int) -> bool:
        # Check if value already exists - avoid duplicates
        if val in self.val_to_index:
            return False
        
        # Add value to end of list - O(1) operation
        self.values.append(val)
        # Store index in dictionary - needed for O(1) removal later
        self.val_to_index[val] = len(self.values) - 1
        return True
    
    def remove(self, val: int) -> bool:
        # Check if value exists - can't remove what's not there
        if val not in self.val_to_index:
            return False
        
        # Get index of value to remove - needed for swap operation
        index_to_remove = self.val_to_index[val]
        # Get last value in list - we'll swap with this
        last_value = self.values[-1]
        
        # Swap value to remove with last value - maintain O(1) removal
        self.values[index_to_remove] = last_value
        # Update index of last value - keep mapping consistent
        self.val_to_index[last_value] = index_to_remove
        
        # Remove value from list - O(1) since it's at the end
        self.values.pop()
        # Remove from dictionary - clean up mapping
        del self.val_to_index[val]
        return True
    
    def getRandom(self) -> int:
        # Return random element from list - O(1) random access
        return random.choice(self.values)
