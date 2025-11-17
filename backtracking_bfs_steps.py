"""
Backtracking and BFS Problem - Compute Steps to Reach Target

Given a starting value of 1 and a sequence of operations (* and +), 
compute the amount of steps taken to reach a given target.

Example:
- Start: 1
- Operations: [*, +, *, +]
- Target: 10
- Find minimum steps to reach target

THOUGHT PROCESS FOR INTERVIEWER:

The challenge is finding the minimum steps to reach a target using operations. Let me think through this:

1. **Problem Analysis**:
   - Start with value 1
   - Apply operations (* and +) to reach target
   - Find minimum number of operations needed
   - Operations can be applied in any order

2. **Approach Options**:
   - **Backtracking**: Try all possible combinations - O(2^n)
   - **BFS**: Explore all possible values level by level - O(2^n)
   - **BFS is better**: Finds minimum steps naturally

3. **Key Insight**: 
   - Use BFS to explore all possible values
   - Track steps taken to reach each value
   - Stop when we reach the target
   - BFS guarantees minimum steps

4. **Example walkthrough with target=10**:
   - Level 0: [1] (0 steps)
   - Level 1: [2, 2] (1 step: 1*2, 1+1)
   - Level 2: [4, 3, 4, 3] (2 steps: 2*2, 2+1, 2*2, 2+1)
   - Continue until we reach 10

This gives us O(2^n) time complexity where n = number of operations!
"""

from collections import deque
from typing import List

class Solution:
    def minStepsToTarget(self, operations: List[str], target: int) -> int:
        """
        Find minimum steps to reach target using BFS.
        
        Args:
            operations: List of operations (* and +)
            target: Target value to reach
            
        Returns:
            Minimum number of steps, or -1 if impossible
        """
        if target == 1:  # Already at target - no steps needed
            return 0
        
        queue = deque([(1, 0)])  # (current_value, steps_taken) - BFS queue
        visited = {1}  # Track visited values to avoid cycles - prevent infinite loops
        
        while queue:
            current_value, steps = queue.popleft()  # Get current state - process each value
            
            # Try all possible operations - explore all possibilities
            for operation in operations:  # Apply each operation to current value
                if operation == '*':  # Multiplication operation - double the value
                    new_value = current_value * 2  # Apply multiplication
                elif operation == '+':  # Addition operation - add 1 to value
                    new_value = current_value + 1  # Apply addition
                else:  # Invalid operation - skip unknown operations
                    continue
                
                # Check if we reached the target - success condition
                if new_value == target:  # Found target with minimum steps
                    return steps + 1  # Return steps taken to reach target
                
                # If value not visited and within reasonable bounds - avoid infinite growth
                if new_value not in visited and new_value <= target * 2:  # Reasonable upper bound
                    visited.add(new_value)  # Mark value as visited - prevent revisiting
                    queue.append((new_value, steps + 1))  # Add to queue with incremented steps
        
        return -1  # Target not reachable - no valid path found
    
    def minStepsToTargetBacktracking(self, operations: List[str], target: int) -> int:
        """
        Alternative backtracking approach to find minimum steps.
        
        Args:
            operations: List of operations (* and +)
            target: Target value to reach
            
        Returns:
            Minimum number of steps, or -1 if impossible
        """
        min_steps = float('inf')  # Track minimum steps found - start with infinity
        
        def backtrack(current_value: int, steps: int, used_operations: List[str]) -> None:
            nonlocal min_steps  # Access outer variable - modify minimum steps
            
            if current_value == target:  # Reached target - found valid path
                min_steps = min(min_steps, steps)  # Update minimum steps - keep best solution
                return  # Stop exploring this path - found solution
            
            if current_value > target:  # Exceeded target - invalid path
                return  # Stop exploring this path - no solution possible
            
            # Try each operation - explore all possibilities
            for i, operation in enumerate(operations):  # Try each operation
                if operation == '*':  # Multiplication operation - double the value
                    new_value = current_value * 2  # Apply multiplication
                elif operation == '+':  # Addition operation - add 1 to value
                    new_value = current_value + 1  # Apply addition
                else:  # Invalid operation - skip unknown operations
                    continue
                
                # Recursively explore with new value - continue search
                backtrack(new_value, steps + 1, used_operations + [operation])  # Explore further
        
        backtrack(1, 0, [])  # Start backtracking from value 1 with 0 steps - begin search
        
        return min_steps if min_steps != float('inf') else -1  # Return minimum steps or -1 if impossible
