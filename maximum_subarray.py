"""
LeetCode #53: Maximum Subarray

Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

THOUGHT PROCESS FOR INTERVIEWER:

**Approach**: Use Kadane's Algorithm - make a greedy choice at each position.

**Key Insight**: 
At each position, we decide: "Should I extend the previous subarray or start fresh from here?"
- If previous sum is negative, it hurts us → start fresh
- If previous sum is positive, it helps us → extend it

**How it works**:
- Keep track of current_sum (best sum ending at current position)
- Keep track of max_sum (best sum found so far)
- At each element:
  - Either add to current_sum OR start fresh (whichever is larger)
  - Update max_sum if current_sum is better

**Example**: nums = [-2,1,-3,4,-1,2,1,-5,4]
- Position 0: current=-2, max=-2
- Position 1: current=1 (start fresh), max=1
- Position 2: current=-2 (1+-3), max=1
- Position 3: current=4 (start fresh), max=4
- Position 4: current=3 (4+-1), max=4
- Position 5: current=5 (3+2), max=5
- Position 6: current=6 (5+1), max=6
- Position 7: current=1 (6+-5), max=6
- Position 8: current=5 (1+4), max=6

**Time**: O(n) - single pass through array
**Space**: O(1) - only use two variables
"""

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        curr_sum = 0

        for i in range(len(nums)):
            curr_sum += nums[i]
            max_sum = max(max_sum, curr_sum)

            if curr_sum < 0:
                curr_sum = 0
        return max_sum

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    print("=== Maximum Subarray Tests ===")
    print()
    
    # Test case 1
    nums1 = [-2,1,-3,4,-1,2,1,-5,4]
    result1 = solution.maxSubArray(nums1)
    print(f"Test 1:")
    print(f"Input: {nums1}")
    print(f"Output: {result1}")
    print(f"Expected: 6")
    print(f"Subarray: [4,-1,2,1]")
    print()
    
    # Test case 2
    nums2 = [1]
    result2 = solution.maxSubArray(nums2)
    print(f"Test 2:")
    print(f"Input: {nums2}")
    print(f"Output: {result2}")
    print(f"Expected: 1")
    print()
    
    # Test case 3
    nums3 = [5,4,-1,7,8]
    result3 = solution.maxSubArray(nums3)
    print(f"Test 3:")
    print(f"Input: {nums3}")
    print(f"Output: {result3}")
    print(f"Expected: 23")
    print()
    
    # Test case 4 - all negative
    nums4 = [-3,-2,-5,-1]
    result4 = solution.maxSubArray(nums4)
    print(f"Test 4 (all negative):")
    print(f"Input: {nums4}")
    print(f"Output: {result4}")
    print(f"Expected: -1")
    print()
    
    # Test case 5 - mix with large negative
    nums5 = [8,-19,5,-4,20]
    result5 = solution.maxSubArray(nums5)
    print(f"Test 5:")
    print(f"Input: {nums5}")
    print(f"Output: {result5}")
    print(f"Expected: 21")
    print(f"Subarray: [5,-4,20]")
    print()
