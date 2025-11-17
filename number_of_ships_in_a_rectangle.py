"""

(This problem has an interactive aspect, but here's the conceptual solution)

Given a rectangle on the plane, count the number of ships in that rectangle.

The rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) is the bottom-left corner and (x2, y2) is the top-right corner.

You can only use the Sea.hasShips() method, which returns true if there is at least one ship in the given rectangle.

Example:
Input: rectangle = [0, 0, 2, 2]
Output: Number of ships in the rectangle

Constraints:
- 0 <= x1 <= x2 <= 1000
- 0 <= y1 <= y2 <= 1000
- At most 10 calls to hasShips().
"""





class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        # Base case: if rectangle is empty, no ships
        if (topRight.x < bottomLeft.x or topRight.y < bottomLeft.y):
            return 0
        
        # Base case: if no ships in this rectangle, return 0
        if not sea.hasShips(topRight, bottomLeft):
            return 0
        
        # Base case: if rectangle is a single point, return 1
        if (topRight.x == bottomLeft.x and topRight.y == bottomLeft.y):
            return 1
        
        # Split rectangle into 4 quadrants
        mid_x = (topRight.x + bottomLeft.x) // 2
        mid_y = (topRight.y + bottomLeft.y) // 2
        
        # Recursively count ships in each quadrant
        return (self.countShips(sea, Point(mid_x, topRight.y), Point(bottomLeft.x, mid_y + 1)) +  # Q3: Top-left quadrant
                self.countShips(sea, Point(topRight.x, topRight.y), Point(mid_x + 1, mid_y + 1)) +  # Q4: Top-right quadrant
                self.countShips(sea, Point(mid_x, mid_y), Point(bottomLeft.x, bottomLeft.y)) +       # Q1: Bottom-left quadrant
                self.countShips(sea, Point(topRight.x, mid_y), Point(mid_x + 1, bottomLeft.y)))     # Q2: Bottom-right quadrant
