"""
LeetCode #209: Minimum Size Subarray Sum

Given an array of positive integers nums and a positive integer target, 
return the minimal length of a contiguous subarray [nums[l], nums[l+1], ..., nums[r-1], nums[r]] 
of which the sum is greater than or equal to target. If there is no such subarray, return 0.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

Two Approaches:
1. Sliding Window: O(n) time, O(1) space
2. Binary Search: O(n log n) time, O(n) space
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        """Sliding Window Approach - O(n) time, O(1) space"""
        left = 0
        current_sum = 0
        min_length = float('inf')
        
        for right in range(len(nums)):
            current_sum += nums[right]
            
            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1
        
        return min_length if min_length != float('inf') else 0
    
    def minSubArrayLenBinarySearch(self, target: int, nums: list[int]) -> int:
        """Binary Search Approach - O(n log n) time, O(n) space"""
        n = len(nums)
        if n == 0:
            return 0
        
        # Build prefix sum array
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        # Binary search on subarray length
        left, right = 1, n
        result = 0
        
        while left <= right:
            mid = (left + right) // 2
            
            # Check if there exists a subarray of length 'mid' with sum >= target
            if self.hasValidSubarray(prefix_sum, target, mid):
                result = mid
                right = mid - 1  # Try smaller length
            else:
                left = mid + 1   # Try larger length
        
        return result
    
    def hasValidSubarray(self, prefix_sum: list[int], target: int, length: int) -> bool:
        """Helper function to check if subarray of given length exists with sum >= target"""
        for i in range(length, len(prefix_sum)):
            # Sum of subarray from (i-length) to (i-1)
            current_sum = prefix_sum[i] - prefix_sum[i - length]
            if current_sum >= target:
                return True
        return False


# Test cases
if __name__ == "__main__":
    solution = Solution()
    nums1 = [2,3,1,2,4,3]
    target1 = 7
    
    print("=== SLIDING WINDOW (O(n)) ===")
    print(f"Input: target={target1}, nums={nums1}")
    print(f"Output: {solution.minSubArrayLen(target1, nums1)}")
    print("Expected: 2")
    print()
    
    print("=== BINARY SEARCH (O(n log n)) ===")
    print(f"Input: target={target1}, nums={nums1}")
    print(f"Output: {solution.minSubArrayLenBinarySearch(target1, nums1)}")
    print("Expected: 2")
    print()
    
    # Test other cases
    print("=== Additional Tests ===")
    test_cases = [
        (4, [1,4,4], 1),
        (11, [1,1,1,1,1,1,1,1], 0),
        (1, [1], 1)
    ]
    
    for target, nums, expected in test_cases:
        sliding_result = solution.minSubArrayLen(target, nums)
        binary_result = solution.minSubArrayLenBinarySearch(target, nums)
        print(f"Target: {target}, Nums: {nums}")
        print(f"Sliding Window: {sliding_result}, Binary Search: {binary_result}, Expected: {expected}")
        print()
