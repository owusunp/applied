"""
LeetCode #268 - Missing Number

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:
Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

Constraints:
- n == nums.length
- 1 <= n <= 10^4
- 0 <= nums[i] <= n
- All the numbers of nums are unique.

THOUGHT PROCESS FOR INTERVIEWER:

**Approach**: Calculate the difference between expected sum and actual sum.

**How it works**:
- Calculate sum of all numbers from 0 to n
- Calculate sum of numbers in the array
- The difference is the missing number

**Key Points**:
- Expected sum = 0 + 1 + 2 + ... + n
- Actual sum = sum of all numbers in array
- Missing number = expected sum - actual sum

**Example**: nums = [3,0,1]
- n = 3 (length of array)
- Expected sum = 0 + 1 + 2 + 3 = 6
- Actual sum = 3 + 0 + 1 = 4
- Missing number = 6 - 4 = 2

**Time Complexity**: O(n) - sum the array once.
**Space Complexity**: O(1) - only use a few variables.
"""

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Find the missing number using sum difference.
        
        Args:
            nums: List of distinct numbers in range [0, n]
            
        Returns:
            The missing number
        """
        # Sum of range [0, n] minus sum of array - the difference is the missing number
        # range(len(nums) + 1) generates 0, 1, 2, ..., n
        # sum(range(...)) gives expected sum, sum(nums) gives actual sum
        return sum(range(len(nums) + 1)) - sum(nums)
