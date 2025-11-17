"""
LeetCode #1 - Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n^2) time complexity?

THOUGHT PROCESS FOR INTERVIEWER:

**Approach**: Use a hashmap to store numbers we've seen and check for complement.

**How it works**:
- For each number, calculate what value we need to reach the target (complement)
- Check if we've already seen that complement in our hashmap
- If yes, return the indices
- If no, store the current number and its index in the hashmap

**Key Points**:
- Hashmap stores {value: index} pairs
- For each number, complement = target - current number
- Check if complement exists in hashmap (O(1) lookup)
- Only need one pass through the array

**Example**: nums = [2,7,11,15], target = 9
- See 2: complement = 9 - 2 = 7, not in map yet, store {2: 0}
- See 7: complement = 9 - 7 = 2, found in map at index 0! Return [0, 1]

**Time Complexity**: O(n) - single pass through array.
**Space Complexity**: O(n) - hashmap stores up to n elements.
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Find two indices whose values sum to target using hashmap.
        
        Args:
            nums: List of integers
            target: Target sum
            
        Returns:
            List of two indices [i, j] where nums[i] + nums[j] = target
        """
        # Hashmap to store {value: index} pairs - track numbers we've seen
        seen = {}
        
        # Iterate through array with index and value - check each number
        for i, num in enumerate(nums):
            # Calculate what number we need to reach target - the complement
            complement = target - num
            
            # Check if complement exists in hashmap - O(1) lookup
            if complement in seen:
                # Found the pair! Return indices - complement index and current index
                return [seen[complement], i]
            
            # Store current number and its index - remember this number for later
            seen[num] = i
        
        # No solution found (though problem guarantees one exists) - should never reach here
        return []

