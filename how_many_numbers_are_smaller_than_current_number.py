"""
LeetCode #1365 - How Many Numbers Are Smaller Than the Current Number

Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. 
That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

Example 1:
Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation: 
- For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
- For nums[1]=1 does not exist any smaller number than it.
- For nums[2]=2 there exist one smaller number than it (1). 
- For nums[3]=2 there exist one smaller number than it (1). 
- For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

Example 2:
Input: nums = [6,5,4,8]
Output: [2,1,0,3]

Example 3:
Input: nums = [7,7,7,7]
Output: [0,0,0,0]

Constraints:
- 2 <= nums.length <= 500
- 0 <= nums[i] <= 100

THOUGHT PROCESS FOR INTERVIEWER:

**Approach**: Sort the array and use a hashmap to track positions.

**How it works**:
- Sort the array to find each number's rank (position)
- The index in sorted array = count of smaller numbers
- Use hashmap to store {number: count of smaller numbers}
- For duplicates, only store the first occurrence (leftmost position)

**Key Points**:
- Sorting gives us the rank of each number
- Index in sorted array = how many numbers are smaller
- Hashmap maps number to its count of smaller numbers
- Handle duplicates by only storing first occurrence

**Example**: nums = [8,1,2,2,3]
- Sorted: [1,2,2,3,8]
- Map: {1:0, 2:1, 3:3, 8:4}
- Result: [4,0,1,1,3]

**Time Complexity**: O(n log n) - sorting dominates.
**Space Complexity**: O(n) - hashmap and sorted array.
"""

from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        """
        Find count of smaller numbers for each element using sorting and hashmap.
        
        Args:
            nums: List of integers
            
        Returns:
            List where each element is count of smaller numbers
        """
        # Sort the array to find rank of each number - sorting helps us determine position
        sorted_nums = sorted(nums)
        
        # Hashmap to store {number: count of smaller numbers} - maps value to its rank
        num_to_count = {}
        
        # Build hashmap from sorted array - assign ranks based on position
        for index, num in enumerate(sorted_nums):
            # Only store first occurrence of each number - for duplicates, keep leftmost position
            # This is because the leftmost position gives us the count of smaller numbers
            if num not in num_to_count:
                num_to_count[num] = index
        
        # Build result by looking up each number in hashmap - get count for each original number
        result = [num_to_count[num] for num in nums]
        
        # Return the result array - counts of smaller numbers for each element
        return result

