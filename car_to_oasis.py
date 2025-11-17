"""
Car to Oasis Problem

Given a 2D matrix that represents a matrix where:
- '.' denotes empty land
- 'c' indicates car (starting point of the car)
- 'o' indicates oasis (the oasis, our destination)
- 's' indicates sand (the car can drive through it)
- 'r' indicates rocks (obstacles that cannot be crossed)
- Integer values represent gas stations (an integer value - a gas station, the car can refill once, as many gas units as the value indicates)

And another integer gas which indicates gas we have left.
Traversing one unit in the matrix consumes 1 gas unit.
You can move up, down, left, and right.

Example: the matrix below and gas = 5 returns true since we can get from c to o in 5 units (1 unit left, 3 units down, and 1 unit right)

[[. . . c .]
 [. . . . .]
 [. . . . .]
 [. . o . .]]

Part A: Check if car can reach oasis or not. (return bool val)
Part B: Now suppose there is a gas station in the matrix somewhere that is denoted by an integer k where k represents the gas
 units that the car will be refuelled. So if k is 2, car will gain gas. Check if car can still reach oasis (with or without gas station).
Part C: Now let's say there's obstacles in the matrix represented by r. how would you check if car can reach oasis?

Example with rocks:
const desert = [
    ['.', '.', '.', 'c'],
    ['.', '.', '.', '.'],
    ['.', 'r', 'r', '.'],
    ['.', '.', 'o', '.'],
]

Example with gas station:
const desert_with_gas = [
    ['.', '.', '.', 'o'],
    ['.', 'r', 'r', '.'],
    ['c', 'c', 'r', 'r'],
    ['c', 'c', '.', 20]
];

Example with sand:
const desert_with_sand = [
    ['.', 's', 's', 'o'],
    ['s', 'r', 'r', 's'],
    ['c', 's', 'r', 'r'],
    ['c', 'c', 's', 20]
];

THOUGHT PROCESS FOR INTERVIEWER:

The challenge is finding a path from car to oasis with limited gas. Let me think through this:

1. **Problem Analysis**:
   - Need to find path from 'c' to 'o'
   - Each move consumes 1 gas unit
   - Can move in 4 directions (up, down, left, right)
   - Need to check if we have enough gas

2. **Approach Options**:
   - **BFS**: Good for finding shortest path, but we need to track gas
   - **DFS**: Can explore all paths, but might be inefficient
   - **BFS with gas tracking**: Best approach - find shortest path while tracking gas

3. **Key Insight**: 
   - Use BFS to find shortest path
   - Track gas remaining at each position
   - If we reach oasis with gas >= 0, return true

4. **Example walkthrough with gas=5**:
   - Start at 'c' with gas=5
   - Move left: gas=4
   - Move down: gas=3
   - Move down: gas=2
   - Move down: gas=1
   - Move right: gas=0
   - Reach 'o' with gas=0 >= 0, return true

This gives us O(m*n) time complexity!
"""

from collections import deque
from typing import List

class Solution:
    def canReachOasis(self, matrix: List[List[str]], gas: int) -> bool:
        # Find the starting position of the car - needed to know where to start BFS
        start_row, start_col = -1, -1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 'c':
                    start_row, start_col = i, j
                    break
        
        if start_row == -1:  # No car found - invalid input
            return False
        
        # BFS queue: (row, col, gas_remaining) - track position and gas at each step
        queue = deque([(start_row, start_col, gas)])
        visited = set()  # Track visited positions to avoid cycles - prevent infinite loops
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up - all possible moves
        
        while queue:
            row, col, current_gas = queue.popleft()  # Get current position and gas - process each state
            
            # Check if we reached the oasis - success condition
            if matrix[row][col] == 'o':
                return True  # Found oasis with enough gas - mission accomplished
            
            # If we're out of gas, can't continue - failure condition
            if current_gas <= 0:
                continue  # Skip this path - no gas to continue
            
            # Explore all 4 directions - try all possible moves
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc  # Calculate new position - move in direction
                
                # Check bounds, if position not visited, and if it's not a rock - valid move and not already explored
                if (0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]) and
                    (new_row, new_col) not in visited and matrix[new_row][new_col] != 'r'):
                    
                    visited.add((new_row, new_col))  # Mark position as visited - prevent revisiting
                    
                    # Check if current position is a gas station (integer value)
                    if isinstance(matrix[new_row][new_col], int):
                        # Refuel at gas station - add gas from the station
                        new_gas = current_gas - 1 + matrix[new_row][new_col]  # Consume 1 gas for move, add station gas
                        queue.append((new_row, new_col, new_gas))  # Add to queue with refueled gas
                    else:
                        # Regular move - consume 1 gas
                        queue.append((new_row, new_col, current_gas - 1))  # Add to queue with 1 less gas - consume gas for move
        
        return False  # No path found to oasis - all paths exhausted
