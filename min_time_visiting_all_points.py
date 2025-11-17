"""
LeetCode #1266 - Minimum Time Visiting All Points

On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi]. Return the minimum time in seconds to visit all the points in the order given by points.

You can move according to these rules:
- In 1 second, you can either:
  - move vertically by one unit,
  - move horizontally by one unit, or
  - move diagonally sqrt(2) units (in other words, move one unit vertically then one unit horizontally in 1 second).

You have to visit the points in the same order as they appear in the array.
You are allowed to pass through points that appear later in the order, but these do not count as visits.

Example 1:
Input: points = [[1,1],[3,4],[-1,0]]
Output: 7
Explanation: One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]   
Time from [1,1] to [3,4] = 3 seconds 
Time from [3,4] to [-1,0] = 4 seconds
Total time = 7 seconds

Example 2:
Input: points = [[3,2],[-2,2]]
Output: 5

Constraints:
- points.length == n
- 1 <= n <= 100
- points[i].length == 2
- -1000 <= points[i][0], points[i][1] <= 1000

THOUGHT PROCESS FOR INTERVIEWER:

**Approach**: Calculate max of absolute differences in x and y coordinates.

**How it works**:
- Between two points, we can move diagonally which covers both x and y simultaneously
- The time needed is the maximum of the x-distance and y-distance
- Why? Because we move diagonally until we align on one axis, then move straight

**Key Insight**:
- Time between two points = max(|x2 - x1|, |y2 - y1|)
- Diagonal movement is the key: move diagonally to cover both dimensions
- Once aligned on one axis, move straight on the other axis

**Example**: From [1,1] to [3,4]
- x-distance = |3 - 1| = 2
- y-distance = |4 - 1| = 3
- Move diagonally 2 times: [1,1] → [2,2] → [3,3]
- Move vertically 1 time: [3,3] → [3,4]
- Total time = max(2, 3) = 3 seconds

**Time Complexity**: O(n) - visit each point once.
**Space Complexity**: O(1) - only use a few variables.
"""

from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        """
        Calculate minimum time to visit all points using diagonal and straight moves.
        
        Args:
            points: List of [x, y] coordinates
            
        Returns:
            Minimum time in seconds to visit all points in order
        """
        # Track total time needed - accumulate time for all segments
        res = 0
        
        # Get starting point - extract first point as current position
        x1, y1 = points.pop()
        
        # Process all remaining points - visit each point in order
        while points:
            # Get next point to visit - pop removes and returns the last point
            x2, y2 = points.pop()
            
            # Calculate time between current and next point - max of x and y distances
            # We move diagonally min(dx, dy) times, then straight the remaining distance
            # Total time = max(abs(x2-x1), abs(y2-y1))
            res += max(abs(x2 - x1), abs(y2 - y1))
            
            # Update current position - move to the point we just visited
            x1, y1 = x2, y2
        
        # Return total time for all segments - sum of all point-to-point times
        return res

