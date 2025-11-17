"""
LeetCode #845 - Longest Mountain in Array

You may recall that an array arr is a mountain array if and only if:
- arr.length >= 3
- There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
  - arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
  - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Given an integer array arr, return the length of the longest subarray that is a mountain. Return 0 if there is no mountain subarray.

Example 1:
Input: arr = [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.

Example 2:
Input: arr = [2,2,2]
Output: 0
Explanation: There is no mountain.

Example 3:
Input: arr = [0,1,2,3,4,5,4,3,2,1,0]
Output: 11
Explanation: The entire array is a mountain.

Constraints:
- 1 <= arr.length <= 10^4
- 0 <= arr[i] <= 10^4

THOUGHT PROCESS FOR INTERVIEWER:

**Approach**: Track increasing (up) and decreasing (down) sequences as we go.

**How it works**:
- Use two counters: up (for increasing) and down (for decreasing)
- As we scan, count consecutive increases and decreases
- A valid mountain needs both up > 0 and down > 0
- Reset counters when we break the pattern

**Key Points**:
- Mountain needs at least 3 elements (up, peak, down)
- Must have both increasing and decreasing parts
- Reset when we see equal elements or start new upward trend after downward
- Length = up + down + 1 (up steps + down steps + peak)

**Example**: arr = [2,1,4,7,3,2,5]
- i=1: 1<2, no up yet
- i=2: 4>1, up=1
- i=3: 7>4, up=2
- i=4: 3<7, down=1, mountain length = 2+1+1 = 4
- i=5: 2<3, down=2, mountain length = 2+2+1 = 5
- i=6: 5>2, reset (new upward after downward)

**Time Complexity**: O(n) - single pass through array.
**Space Complexity**: O(1) - only use a few variables.
"""

from typing import List

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        """
        Find the longest mountain subarray.
        
        Args:
            arr: List of integers
            
        Returns:
            Length of longest mountain, or 0 if none exists
        """
        # Track longest mountain found so far - store the best result
        longest = 0
        
        # Track length of current increasing sequence - count upward steps
        up = 0
        
        # Track length of current decreasing sequence - count downward steps
        down = 0
        
        # Iterate through array starting from second element - compare with previous
        for i in range(1, len(arr)):
            # Reset if we start going up after going down, or if equal elements - break mountain pattern
            # This happens when we hit a valley or plateau
            if (down and arr[i-1] < arr[i]) or (arr[i-1] == arr[i]):
                up = down = 0  # Start fresh - previous mountain ended
            
            # If current element is greater, we're going up - increment up counter
            if arr[i-1] < arr[i]:
                up += 1
            
            # If current element is smaller, we're going down - increment down counter
            if arr[i-1] > arr[i]:
                down += 1
            
            # If we have both up and down, we have a valid mountain - check if it's the longest
            # Mountain length = up steps + down steps + 1 (for the peak)
            if up and down:
                longest = max(longest, up + down + 1)
        
        # Return the longest mountain length found - 0 if no mountain exists
        return longest

